from typing import List
import matplotlib.pyplot as plt

from data_retriever import float_to_time
from data_retriever.DataRetriever import DataRetriever
from data_retriever.Lap import Lap
from data_retriever.RaceFinish import RaceFinish
from f1_plot.F1Plot import F1Plot


class DriverListLapTimesF1Plot(F1Plot):
    def __init__(self, season: int, race_round: int, driver_list: list, data_retriever: DataRetriever):
        self.season = season
        self.race_round = race_round
        self.driver_surname_list = driver_list
        self.retriever = data_retriever

    def __load_data__(self) -> (dict, dict):
        race_finishes: List[RaceFinish] = self.retriever.get_race_standings(self.season, self.race_round)
        driver_dict = {}
        for i in race_finishes:
            if i.get_driver_id() not in self.driver_surname_list:
                continue
            laps : List[Lap] = self.retriever.get_driver_laps(i.get_driver_id(), self.season, self.race_round)
            driver_dict[i.get_driver_id()] = laps
        drivers_data_dict = dict()
        for driver_id in driver_dict:
            drivers_data_dict[driver_id] = self.retriever.get_driver_info(driver_id=driver_id)
        return driver_dict, drivers_data_dict

    def plot(self, to_file: str = "./f1_plot.png") -> None:
        driver_dict, drivers_data_dict = self.__load_data__()
        for driver in driver_dict:
            y_driver = list(map( lambda x: x.get_time_millis(), driver_dict[driver]))
            x_driver = list(range(0, len(driver_dict[driver])))
            driver_name = drivers_data_dict[driver].get_full_name() if driver in drivers_data_dict else driver
            plt.plot(x_driver, y_driver, "o",markersize=3,label=driver_name)
        plt.legend()
        locs, labels = plt.yticks()
        plt.yticks(locs, [ float_to_time(i) for i in locs ])
        plt.xlabel("Time")
        plt.xlabel("Laps")
        plt.savefig(to_file)
