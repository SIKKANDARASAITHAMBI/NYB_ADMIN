import time

from features.Inventory.pages.base_page import BasePage
from features.Inventory.utilities import ConfigReader


class UrlVerification(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def order_urls(self):
        page = self.page_title()
        actual_url = self.get_page_url()
        expected_url = None

        if page == "Select Create Order to change | NYB DISTRIBUTORS":
            time.sleep(3)
           # print(actual_url)
            #actual_url = self.get_page_url()
            actual_url =  self.get_page_url()
            expected_url = ConfigReader.urls("URL", "CREATE_ORDER_URL")
            assert expected_url == actual_url

        elif page == "Select Order Received to view | NYB DISTRIBUTORS":
            time.sleep(3)
            actual_url = self.get_page_url()
            expected_url = ConfigReader.urls("URL", "ORDER_RECEIVED")
            assert expected_url == actual_url

        return expected_url, actual_url

    def inventory_urls(self):
        page = self.page_title()
        actual_url = self.get_page_url()
        expected_url = None

        if page == "Select 1.Create Inbound Inventory to change | NYB DISTRIBUTORS":
            time.sleep(0.5)
            expected_url = ConfigReader.urls("URL", "CREATE_INBOUND_INVENTORY_URL")
            assert expected_url == actual_url

        elif page == "Select 5. Vendor Invoices & Packing Slip to change | NYB DISTRIBUTORS":
            time.sleep(0.5)
            expected_url = ConfigReader.urls("URL", "INVOICE_AND_PACKING_SLIP_URL")
            assert expected_url == actual_url

        return expected_url, actual_url