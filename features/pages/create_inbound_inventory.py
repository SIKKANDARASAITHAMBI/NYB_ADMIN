import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By

from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class CreateVendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    document_type_id = "select2-source_id-container"
    search_field_xpath = "//*[@type='search']"
    warehouse_field_id = "select2-warehouse_id-container"
    vendor_field_id = "select2-supplier_id-container"
    packing_slip_no_id = "packing_slip"
    packing_slip_upload = "packing_slip_upload"

    def document_type(self, category, key):
        self.click_element("document_type_id", self.document_type_id)
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def upload_packing_slip(self):
        file_input = self.driver.find_element(By.ID, 'packing_slip_upload')

        # Provide the file path to the file input element
        file_path = "80 kb.jpeg"  # Update this path with the path to the file you want to upload
        file_input.send_keys(file_path)

    def warehouse(self, category, key):
        self.click_element("warehouse_field_id", self.warehouse_field_id)
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def vendors(self, category, key):
        self.click_element("vendor_field_id", self.vendor_field_id)
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def no(self, category, key):
        self.send_value_to_element("packing_slip_no_id", self.packing_slip_no_id,
                                   ConfigReader.create_inbound_inventory(category, key))

    def create_vendor_packingslip(self):
        time.sleep(5)
        self.document_type("VALID INPUTS", "SOURCE_TYPE01")
        time.sleep(5)
        self.warehouse("VALID INPUTS", "WAREHOUSE")
        time.sleep(5)
        self.vendors("VALID INPUTS", "VENDORS")
        time.sleep(5)
        self.no("VALID INPUTS", "NO")
        time.sleep(5)
        self.upload_packing_slip()
