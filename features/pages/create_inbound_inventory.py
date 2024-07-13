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
    packing_slip_date_id = "packing_slip_date"
    packing_slip_received_date_id = "packing_slip_received_date"
    purchase_order_no_id = "purchase_order_no"
    purchase_order_date_id = "purchase_order_date"
    packing_slip_upload = "packing_slip_upload"
    add_product_field_id = "select2-product_id-container"
    inward_qty_xpath = "(//table//tbody//td//input[@class='form-control order_quantity'])[1]"
    damaged_qty_xpath = "(//table//tbody//td//input[@class='form-control damaged_quantity'])[1]"
    batch_no_xpath = "(//table//tbody//td//input[@class='form-control batch_number'])[1]"
    expiry_date_xpath = "(//table//tbody//td//input[@class='form-control expiry_date'])[1]"
    submit_btn_id = "submitbutton"
    click_random_xpath = "(//*[@class='form-row'])"

    def search(self, category, key):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def document_type(self, category, key):
        self.click_element("document_type_id", self.document_type_id)
        self.search(category, key)

    def warehouse(self, category, key):
        self.click_element("warehouse_field_id", self.warehouse_field_id)
        self.search(category, key)

    def vendors(self, category, key):
        self.click_element("vendor_field_id", self.vendor_field_id)
        self.search(category, key)

    def no(self, category, key):
        self.send_value_to_element("packing_slip_no_id", self.packing_slip_no_id,
                                   ConfigReader.create_inbound_inventory(category, key))

    def date(self, category, packing_slip_date):
        self.clear_element("packing_slip_date_id", self.packing_slip_date_id)
        self.send_value_to_element(
            "packing_slip_date_id", self.packing_slip_date_id,
            ConfigReader.create_inbound_inventory(
                category, packing_slip_date))
        self.click_element("click_random_xpath", self.click_random_xpath)

    def received_date(self, category, packing_slip_received_date):
        self.clear_element("packing_slip_received_date_id", self.packing_slip_received_date_id)
        self.send_value_to_element(
            "packing_slip_received_date_id", self.packing_slip_received_date_id,
            ConfigReader.create_inbound_inventory(
                category, packing_slip_received_date))
        self.click_element("click_random_xpath", self.click_random_xpath)

    def purchase_order_no(self, category, purchase_order_no):
        self.clear_element("purchase_order_no_id", self.purchase_order_no_id)
        self.send_value_to_element(
            "purchase_order_no_id", self.purchase_order_no_id,
            ConfigReader.create_inbound_inventory(
                category, purchase_order_no))

    def purchase_order_date(self, category, purchase_order_date):
        self.clear_element("purchase_order_date_id", self.purchase_order_date_id)
        self.send_value_to_element(
            "purchase_order_date_id", self.purchase_order_date_id,
            ConfigReader.create_inbound_inventory(
                category, purchase_order_date))
        self.click_element("click_random_xpath", self.click_random_xpath)

    def upload_packing_slip(self):
        file_input = self.driver.find_element(By.ID, 'packing_slip_upload')
        file_path = "C:/Users/sikku/Downloads/images.png"
        file_input.send_keys(file_path)

    def add_products(self, category, product):
        self.click_element("add_product_field_id", self.add_product_field_id)
        self.search(category, product)

    def inward_quantity(self, category, inward_quantity):
        self.send_value_to_element("inward_qty_xpath", self.inward_qty_xpath
                                   , ConfigReader.create_inbound_inventory(category, inward_quantity))

    def damaged_quantity(self, category, damaged_quantity):
        self.click_element("damaged_qty_xpath", self.damaged_qty_xpath)
        self.clear_element("damaged_qty_xpath", self.damaged_qty_xpath)
        self.send_value_to_element("damaged_qty_xpath", self.damaged_qty_xpath
                                   , ConfigReader.create_inbound_inventory(category, damaged_quantity))

    def batch_number(self, category, batch_no):
        self.send_value_to_element(
            "batch_no_xpath", self.batch_no_xpath, ConfigReader.create_inbound_inventory(
                category, batch_no))

    def expiry_date(self, category, expiry_date):
        self.send_value_to_element(
            "expiry_date_xpath", self.expiry_date_xpath, ConfigReader.create_inbound_inventory(
                category, expiry_date))

    def submit(self):
        self.click_element("submit_btn_id", self.submit_btn_id)