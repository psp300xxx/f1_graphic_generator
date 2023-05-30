# This is a sample Python script.
import argparse

from data_retriever.ErgastRetriever import ErgastRetriever
from f1_plot.DriverListLapTimesF1Plot import DriverListLapTimesF1Plot
from f1_plot.FirstNLapTimesF1Plot import FirstNLapTimesF1Plot


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

parser = argparse.ArgumentParser(
                    prog = 'F1 Graphic Generator',
                    description = 'Using this tool you will be able to generate graphic for the standings of the F1 Races',
                )

parser.add_argument("-season", type=int, required=True)
parser.add_argument("-round", type=int, required=True)
parser.add_argument("-n", type=int, default=2)
parser.add_argument("-driverList", type=str, default=None)

def parseDriverList(driver_list: str) -> list:
    drivers = driver_list.split(",")
    return list(drivers)

def main():
    args = parser.parse_args()
    season = args.season
    race_round = args.round
    n = args.n
    driver_list = args.driverList
    if driver_list is not None:
        driver_list = parseDriverList(driver_list)
    retriever = ErgastRetriever()
    if driver_list is not None:
        plotter = DriverListLapTimesF1Plot(season=season, race_round=race_round, driver_list=driver_list, data_retriever=retriever)
    else:
        plotter = FirstNLapTimesF1Plot(season=season, race_round=race_round, n=n, data_retriever=retriever)
    plotter.plot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
