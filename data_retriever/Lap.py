# import Utils
from data_retriever import time_to_float


class Lap(object):
    def __init__(self, driver_id : str, time : str, position : int, lap_number: int):
        self.driver = driver_id
        self.time = time
        self.position = position
        self.lap_number = lap_number

    def get_driver_id(self) -> str:
        return self.driver

    def get_position(self):
        return self.position

    def get_lap_number(self):
        return self.lap_number


    def get_time_str(self) -> str:
        return self.time

    def get_time_millis(self) -> float:
        return time_to_float(self.time)
