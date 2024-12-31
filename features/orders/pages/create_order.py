import time
from lib2to3.fixes.fix_input import context

from selenium.common import exceptions, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from features.Inventory.pages.create_inbound_inventory import CreateVendorPackingSlip

from features.orders.pages.base_page import BasePage
from features.orders.utilities import ConfigReader


class CreateOrder(BasePage, CreateVendorPackingSlip):

    def __init__(self, driver):
        super().__init__(driver)

    # def search1(self):
    #     search = self.locate_element("search_field_xpath", self.search_field_xpath)
    #     time.sleep(0.5)
    #     actions = ActionChains(self.driver)
    #     actions.send_keys_to_element(search, self)
    #     actions.send_keys(Keys.ENTER)
    #     actions.perform()

    branch_type_xpath = "//span[@id='select2-branch_id-container']"
    # branch_type_xpath = "(//span[@role='presentation']//b)[1]"
    def branch(self, branch_name):
        time.sleep(5)
        self.click_element("branch_type_xpath", self.branch_type_xpath)
        time.sleep(5)
        print(branch_name)
        self.search1(branch_name)

    def filters(self, value):

        if value == "Branch type":
            self.click_element("branch_type_xpath", self.branch_type_xpath)
            self.search("VALID INPUTS", "SOURCE_TYPE05")
        elif value == "Warehouse":
            pass
        elif value == "Vendors":
            pass
        #elif value == "Document No":
            #self.get_success_message()
            #self.send_value_to_element("document_no_xpath", self.document_no_xpath, self.doc_number)
        self.click_element("submit_btn_id", self.submit_btn_id)

    add_product_order_xpath = "//span[@id='select2-product_id-container']"
    def add_products(self, product_list: list):
        count = len(product_list)
        for index in range(count):
            self.click_element("add_product_order_xpath", self.add_product_order_xpath)
            self.search1(product_list[index])
        time.sleep(1)

    payment_mode_id = "select2-payment_mode_del-container"

    def payment(self, payment_mode):
        time.sleep(5)
        self.click_element("payment_mode_id", self.payment_mode_id)
        time.sleep(5)
        print(payment_mode)
        self.search1(payment_mode)

    def submit_order(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Submit Order']"))
        )

        submit_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Submit Order']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(submit_btn).click().perform()

    def Verify_account(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[text() = 'Yes'])[1]"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Yes'])[1]"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()
    def verify_order_received_url(context):
        context.driver.implicitly_wait(20)
        context.url = UrlVerification(context.driver)
        print(context.url)
        context.url.order_urls("Order Received")

    order_no_id = "(//span[text()='/'])[2]/following::input[1]"

    def Verify_Order_Placed(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[text() = 'Ok'])"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text() = 'Ok'])"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()
    def order_no(self, category, key):
        self.send_value_to_element("order_no_id", self.order_no_id,
                                   ConfigReader.create_order(category, key))

    def Order_Received_Page(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text() = '1. Order Received']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text() = '1. Order Received']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()