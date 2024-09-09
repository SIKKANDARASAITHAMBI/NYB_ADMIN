import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

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
    add_sample_product_field_id = "select2-product_dropdown-container"
    sample_product_check_box_xpath = "//table//tbody//td//input[@type='checkbox']"
    sample_product_name_xpath = "//table//tbody//td//input[@placeholder='Enter Product Name']"
    sample_flavor_name_xpath = "//table//tbody//td//input[@placeholder='Enter Flavor Name']"
    sample_size_weight_variant_name_xpath = "//table//tbody//td//input[@placeholder='Enter Size/Weight']"
    sample_product_price_field_xpath = "//table//tbody//td//input[@placeholder='Enter Price']"
    confirm_btn_id = "confirmButton"
    added_products_table_xpath = "//table[@id='tblpackingslip']//tbody[@id='packingtbody']//tr"
    inward_qty_xpath = "td"
    damaged_qty_xpath = "td"
    unit_price_xpath = "td"
    batch_no_xpath = "td"
    expiry_date_xpath = "td"
    submit_btn_xpath = "//button[text()='Submit']"
    click_random_xpath = "(//*[@class='form-row'])"
    add_product_xpath = "(//*[text()='Add New Product'])[2]"

    def search(self, category, key):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(1)
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
        file_path = " C:/Users/Dell/Downloads/packing-slip-2x (1).png"
        file_input.send_keys(file_path)

    def add_products(self, *args):
        product_count = len(args[1])
        for index in range(product_count):
            category = args[0]
            product = args[1][index]
            self.click_element("add_product_field_id", self.add_product_field_id)
            self.search(category, product)

    def add_sample_products(self, category, sample_product):

        #It is statically written, due to search issues for time being this is structured like this.
        self.click_element("add_sample_product_field_id", self.add_sample_product_field_id)
        self.click_element("add_product_xpath", self.add_product_xpath)

    def is_sample_product(self):
        self.click_element(
            "sample_product_check_box_xpath", self.sample_product_check_box_xpath)

    #NEED TO WORK HERE#
    def sample_product_name(self, category, sample_product_name):
        self.send_value_to_element(
            "sample_product_name_xpath", self.sample_product_name_xpath,
            ConfigReader.create_inbound_inventory(category, sample_product_name))

    def sample_products_flavor_name(self, category, sample_product_flavor_name):
        self.send_value_to_element(
            "sample_flavor_name_xpath", self.sample_flavor_name_xpath,
            ConfigReader.create_inbound_inventory(category, sample_product_flavor_name))

    def sample_product_flavors_size_weight_variant_name(self, category,
                                                        sample_product_flavors_size_weight_variant_name):
        self.send_value_to_element(
            "sample_flavor_name_xpath", self.sample_flavor_name_xpath,
            ConfigReader.create_inbound_inventory(category, sample_product_flavors_size_weight_variant_name))

    def confirm(self):
        self.click_element("confirm_btn_id", self.confirm_btn_id)

    #Static Code.

    # def inward_quantity(self, category, inward_quantity):
    #     inward_qty = self.locate_element("inward_qty_xpath", self.inward_qty_xpath)
    #     self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'})", inward_qty)
    #     self.send_value_to_element("inward_qty_xpath", self.inward_qty_xpath
    #                                , ConfigReader.create_inbound_inventory(category, inward_quantity))
    #
    # def damaged_quantity(self, category, damaged_quantity):
    #     self.clear_element("damaged_qty_xpath", self.damaged_qty_xpath)
    #     self.send_value_to_element("damaged_qty_xpath", self.damaged_qty_xpath
    #                                , ConfigReader.create_inbound_inventory(category, damaged_quantity))
    #
    # def unit_price(self, category, unit_price):
    #     actual_text = self.get_element_text("unit_price_xpath", self.unit_price_xpath)
    #     if actual_text == "":
    #         #self.clear_element("unit_price_xpath", self.unit_price_xpath)
    #         self.send_value_to_element("unit_price_xpath", self.unit_price_xpath
    #                                    , ConfigReader.create_inbound_inventory(category, unit_price))
    #     else:
    #         pass
    #
    # def batch_number(self, category, batch_no):
    #     self.send_value_to_element(
    #         "batch_no_xpath", self.batch_no_xpath, ConfigReader.create_inbound_inventory(
    #             category, batch_no))
    #
    # def expiry_date(self, category, expiry_date):
    #     self.send_value_to_element(
    #         "expiry_date_xpath", self.expiry_date_xpath, ConfigReader.create_inbound_inventory(
    #             category, expiry_date))

    # Dynamic Code.
    def vendor_packing_slip_table(self, category, inward_quantity, damaged_quantity, unit_price, batch_number,
                                  expiry_date):
        rows = self.mul_elememts(
            "added_products_table_xpath", self.added_products_table_xpath)
        element_count = len(rows)
        for index in range(element_count):
            time.sleep(1)
            # Inward quantity.
            inward_qty = 4
            inward_qty_cell = rows[index].find_elements(By.TAG_NAME, 'td')[inward_qty]
            inward_qty_input = inward_qty_cell.find_element(By.TAG_NAME, 'input')
            inward_qty_input.clear()
            inward_qty_input.send_keys(ConfigReader.create_inbound_inventory(category, inward_quantity[index]))

            # Damaged quantity.
            damaged_qty = 5
            damaged_qty_cell = rows[index].find_elements(By.TAG_NAME, 'td')[damaged_qty]
            damaged_qty_input = damaged_qty_cell.find_element(By.TAG_NAME, 'input')
            damaged_qty_input.send_keys(ConfigReader.create_inbound_inventory(category, damaged_quantity[index]))

            # Unit price. --> In vendor packing slip no price will be available.
            # unit_price_index = 7
            # unit_price_cell = rows[index].find_elements(By.TAG_NAME, 'td')[unit_price_index]
            # unit_price_input = unit_price_cell.find_element(By.TAG_NAME, 'input')
            # time.sleep(5)
            # unit_price_input.send_keys(ConfigReader.create_inbound_inventory(category, unit_price[index]))

            # Batch number.
            batch_number_index = 8
            batch_number_cell = rows[index].find_elements(By.TAG_NAME, 'td')[batch_number_index]
            batch_number_input = batch_number_cell.find_element(By.TAG_NAME, 'input')
            batch_number_input.send_keys(ConfigReader.create_inbound_inventory(category, batch_number[index]))

            # Expiry date.
            expiry_date_index = 9
            expiry_date_cell = rows[index].find_elements(By.TAG_NAME, 'td')[expiry_date_index]
            expiry_date_cell_input = expiry_date_cell.find_element(By.TAG_NAME, 'input')
            expiry_date_cell_input.send_keys(ConfigReader.create_inbound_inventory(category, expiry_date[index]))

    def submit(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Submit']"))
        )

        submit_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_btn).click().perform()
