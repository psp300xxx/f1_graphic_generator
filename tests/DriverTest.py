import unittest

from data_retriever.ErgastRetriever import ErgastRetriever


class DriverTest(unittest.TestCase):

    def test_testing_driver_info_creation(self):
        retriever = ErgastRetriever()
        driver = retriever.get_driver_info(driver_id="alonso")
        self.assertEqual("Fernando", driver.get_name())
        self.assertEqual("Alonso", driver.get_surname())