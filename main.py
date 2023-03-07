# This is a sample Python script.
import argparse

from data_retriever.ErgastRetriever import ErgastRetriever
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

def main():
    args = parser.parse_args()
    season = args.season
    race_round = args.round
    n = args.n
    retriever = ErgastRetriever()
    plotter = FirstNLapTimesF1Plot(season=season, race_round=race_round, n=n, data_retriever=retriever)
    plotter.plot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
