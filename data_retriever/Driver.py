class Driver(object):
    def __init__(self, name: str, surname: str, driver_id: str):
        self.name = name
        self.surname = surname
        self.driver_id = driver_id

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_full_name(self) -> str:
        return self.name + " " + self.surname

    def get_driver_id(self):
        return self.driver_id
