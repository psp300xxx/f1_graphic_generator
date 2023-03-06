class RaceFinish(object):
    def __init__(self, position: int, driver_id : str, points_gained: int):
        self.position = position
        self.driver_id = driver_id
        self.points_gained = points_gained

    def get_position(self) -> int:
        return self.position

    def get_driver_id(self)-> str:
        return self.driver_id

    def get_points_gained(self) -> int:
        return self.points_gained