from typing import List
import requests
from data_retriever.DataRetriever import DataRetriever
from data_retriever.Driver import Driver
from data_retriever.Lap import Lap
import json

from data_retriever.RaceFinish import RaceFinish

ENDPOINT_TEMPLATE = "http://ergast.com/api/f1/{}/{}/drivers/{}/laps.json?limit=78&offset=0"

RACE_RESULT_TEMPLATE = "http://ergast.com/api/f1/{}/{}/results.json"

DRIVER_INFO_TEMPLATE = "http://ergast.com/api/f1/drivers/{}.json"


def get_endpoint(driver_id: str, season: int, race_round: int) -> str:
    return ENDPOINT_TEMPLATE.format(season, race_round, driver_id)

def get_driver_info_endpoint(driver_id: str) -> str:
    return DRIVER_INFO_TEMPLATE.format(driver_id)

def get_race_result_endpoint(season: int, race_round: int) -> str:
    return RACE_RESULT_TEMPLATE.format(season, race_round)

JSON_ROOT_OBJECT = "MRData"

class ErgastRetriever(DataRetriever):

    def get_driver_laps(self, driver_id: str, season: int, race_round: int) -> List[Lap]:
        endpoint = get_endpoint(driver_id, season, race_round)
        response = requests.get(endpoint)
        if not response.status_code == 200:
            return list()
        json_string = response.content.decode('utf8').replace("'", '"')
        json_value = json.loads(json_string)
        lap_array = json_value[JSON_ROOT_OBJECT]["RaceTable"]["Races"][0]["Laps"]
        result = list()
        for lap_json_obj in lap_array:
            new_lap = Lap( driver_id=driver_id, time=lap_json_obj["Timings"][0]['time'], position=int(lap_json_obj["Timings"][0]['position']), lap_number=int(lap_json_obj["number"]))
            result.append(new_lap)
        return result

    def get_race_standings(self, season: int, race_round: int) -> list:
        endpoint = get_race_result_endpoint(season, race_round)
        response = requests.get(endpoint)
        if not response.status_code == 200:
            return list()
        json_string = response.content.decode('utf8').replace("'", '"')
        json_value = json.loads(json_string)
        race_standings = json_value[JSON_ROOT_OBJECT]["RaceTable"]["Races"][0]["Results"]
        result = list()
        for obj in race_standings:
            new_finish = RaceFinish(position=int(obj["position"]), driver_id=obj["Driver"]["driverId"], points_gained=obj["points"])
            result.append(new_finish)
        return result

    def get_driver_info(self, driver_id: str) -> Driver:
        endpoint = get_driver_info_endpoint(driver_id)
        response = requests.get(endpoint)
        if not response.status_code == 200:
            return None
        json_string = response.content.decode('utf8').replace("'", '"')
        json_value = json.loads(json_string)
        return Driver(name=json_value[JSON_ROOT_OBJECT]["DriverTable"]["Drivers"][0]["givenName"], surname=json_value[JSON_ROOT_OBJECT]["DriverTable"]["Drivers"][0]["familyName"], driver_id=driver_id)


