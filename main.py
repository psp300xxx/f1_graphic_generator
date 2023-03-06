# This is a sample Python script.
from data_retriever.ErgastRetriever import ErgastRetriever
from f1_plot.FirstNLapTimesF1Plot import FirstNLapTimesF1Plot


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def main():
    retriever = ErgastRetriever()
    plotter = FirstNLapTimesF1Plot(season=2001, race_round=1, n=2, data_retriever=retriever)
    plotter.plot()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
