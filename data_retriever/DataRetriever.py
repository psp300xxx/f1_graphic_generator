from typing import List

from data_retriever.Lap import Lap


class DataRetriever(object):
    def get_driver_laps(self, driver_id: str, season: int, race_round: int) -> List[Lap]:
        pass

    def get_race_standings(self, season: int, race_round: int) -> list:
        pass
