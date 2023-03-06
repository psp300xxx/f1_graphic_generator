from typing import List
import matplotlib.pyplot as plt
from data_retriever.DataRetriever import DataRetriever
from data_retriever.Lap import Lap
from data_retriever.RaceFinish import RaceFinish
from f1_plot.F1Plot import F1Plot


class FirstNLapTimesF1Plot(F1Plot):
    def __init__(self, season: int, race_round: int, n: int, data_retriever: DataRetriever):
        self.season = season
        self.race_round = race_round
        self.n = n
        self.retriever = data_retriever

    def __load_data__(self) -> dict:
        race_finishes: List[RaceFinish] = self.retriever.get_race_standings(self.season, self.race_round)
        driver_dict = {}
        for i in race_finishes:
            if not i.get_position() <= self.n:
                continue
            laps : List[Lap] = self.retriever.get_driver_laps(i.get_driver_id(), self.season, self.race_round)
            driver_dict[i.get_driver_id()] = laps
        return driver_dict

    def plot(self, to_file: str = "./f1_plot.png") -> None:
        driver_dict = self.__load_data__()
        for driver in driver_dict:
            y_driver = list(map( lambda x: x.get_time_millis(), driver_dict[driver]))
            x_driver = list(range(0, len(driver_dict[driver])))
            plt.plot(x_driver, y_driver, "o",markersize=3,label=driver)
        plt.legend()
        plt.savefig(to_file)
