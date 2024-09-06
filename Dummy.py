import time

from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage
from features.utilities import ConfigReader

class test(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    added_products_table_xpath = "//table[@id='tblpackingslip']//tbody[@id='packingtbody']//tr"
    submit_btn_xpath = "//button[text()='Submit']"
    click_random_xpath = "(//*[@class='form-row'])"
    add_product_xpath = "(//*[text()='Add New Product'])[2]"

    def table_rows(self, category, inward_quantity, damaged_quantity, unit_price, batch_number, expiry_date):
        rows = self.mul_elememts(
            "added_products_table_xpath", self.added_products_table_xpath)
        element_count = len(rows)
        print(element_count)
        for index in range(element_count):
            # Inward quantity.
            inward_qty = 4
            inward_qty_cell = rows[index].find_elements(By.TAG_NAME, 'td')[inward_qty]
            inward_qty_input = inward_qty_cell.find_element(By.TAG_NAME, 'input')
            inward_qty_input.clear()
            inward_qty_input.send_keys(ConfigReader.create_inbound_inventory(category, inward_quantity))

            # Damaged quantity.
            damaged_qty = 6
            damaged_qty_cell = rows[index].find_elements(By.TAG_NAME, 'td')[damaged_qty]
            damaged_qty_input = damaged_qty_cell.find_element(By.TAG_NAME, 'input')
            damaged_qty_input.send_keys(ConfigReader.create_inbound_inventory(category,damaged_quantity))

            #Unit price.
            unit_price_index = 7
            unit_price_cell = rows[index].find_elements(By.TAG_NAME, 'td')[unit_price_index]
            unit_price_input = unit_price_cell.find_element(By.TAG_NAME, 'input')
            unit_price_input.send_keys(ConfigReader.create_inbound_inventory(category, unit_price))

            #Batch number.
            batch_number_index = 8
            batch_number_cell = rows[index].find_elements(By.TAG_NAME, 'td')[batch_number_index]
            batch_number_input = batch_number_cell.find_element(By.TAG_NAME, 'input')
            batch_number_input.send_keys(ConfigReader.create_inbound_inventory(category, batch_number))

            #Expiry date.
            expiry_date_index = 9
            expiry_date_cell = rows[index].find_elements(By.TAG_NAME, 'td')[expiry_date_index]
            expiry_date_cell_input = expiry_date_cell.find_element(By.TAG_NAME, 'input')
            expiry_date_cell_input.send_keys(ConfigReader.create_inbound_inventory(category, expiry_date))