import time

from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class UrlVerification(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def order_urls(self, page):
        if page == "order" or "create order":
            time.sleep(3)
            actual_url = self.get_page_url()
            print(actual_url)
            expected_url = ConfigReader.urls("URL", "CREATE_ORDER_URL")
            assert expected_url == actual_url
            return True

    def inventory_urls(self, page):
        if page == "inventory" or "create inbound inventory":
            time.sleep(3)
            actual_url = self.get_page_url()
            expected_url = ConfigReader.urls("URL", "CREATE_INBOUND_INVENTORY_URL")
            print(actual_url)
            assert expected_url == actual_url
            return True
        elif page  == "invoice and packing slip":
            time.sleep(3)
            actual_url = self.get_page_url()
            expected_url = ConfigReader.urls("URL", "INVOICE_AND_PACKING_SLIP_URL")
            print(actual_url)
            assert expected_url == actual_url
            return True
        elif page == "inbound_inventory_report":
            time.sleep(3)
            actual_url = self.get_page_url()
            expected_url = ConfigReader.urls("URL", "INBOUND_INVENTORY_REPORT")
            print(actual_url)
            assert expected_url == actual_url
            return True