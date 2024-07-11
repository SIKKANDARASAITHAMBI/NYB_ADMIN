import time

from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class UrlVerification(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def create_order_url(self):
        time.sleep(2)
        actual_url = self.get_page_url()
        print(actual_url)
        expected_url = ConfigReader.urls("URL", "CREATE_ORDER_URL")
        assert expected_url == actual_url
        return True

    def create_inbound_inventory_url(self):
        time.sleep(2)
        actual_url = self.get_page_url()
        expected_url = ConfigReader.urls("URL", "CREATE_INBOUND_INVENTORY_URL")
        assert expected_url == actual_url
        return True