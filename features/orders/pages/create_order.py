import time
from lib2to3.fixes.fix_input import context

from selenium.common import exceptions, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from features.Inventory.pages.create_inbound_inventory import CreateVendorPackingSlip
import re
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

    def payment(self, PAYMENT_MODE2):
        time.sleep(5)
        self.click_element("payment_mode_id", self.payment_mode_id)
        time.sleep(5)
        print(PAYMENT_MODE2)
        self.search1(PAYMENT_MODE2)

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

    order_no_id = "searchbar"

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



    def search3(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='submit']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()


    def view_order(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//a[text() = 'View Order'])[1]"))
        )

        view_order = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text() = 'View Order']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(view_order).click().perform()

    def edit_order(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text() = 'Edit Order']"))
        )

        edit_order = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Edit Order']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(edit_order).click().perform()
        time.sleep(5)

    def generate_picking_slip(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@data-confirm='1']"))
        )

        picking_slip = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-confirm='1']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(picking_slip).click().perform()
    def edit_order_confirmation_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='button']"))
        )

        picking_slip = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='button']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(picking_slip).click().perform()

    def download_picking_slip_button(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Download / Print Picking Slip']"))
        )

        download_picking_slip = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Download / Print Picking Slip']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(download_picking_slip).click().perform()
        time.sleep(10)



    def edit_order_data(context):
        # Set up the WebDriver
        context.driver = webdriver.Chrome()  # or webdriver.Firefox() for Firefox users

        # Open the desired webpage
        context.driver.get('https://uat.nybdistributor.com:3000/media/picking-slip/NYB-0102-021214.pdf?ref=0')

        # Locate the element (using XPath in this case)
        element = context.driver.find_element_by_id('editOrderForm')

        # Extract the text and store it in a variable
        data_variable = element.text

        # Close the WebDriver
        context.driver.quit()

        # Output the stored data
        print(data_variable)

    def picking_slip_and_shipment_page(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text() = '2. Picking Slip & Shipment Preparation']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text() = '2. Picking Slip & Shipment Preparation']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def edit_order_validate_picking_slip(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[text() = 'Edit Order /']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text() = 'Edit Order /']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def validation(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id = 'total_picked']")))

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id = 'total_picked']")))
        verify_btn.send_keys('6' + Keys.RETURN)

        #verify_btn.send_keys("Your text here" + Keys.RETURN)

        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    driver_id = "driver_id"
    driver_xpath = "//option[text() = 'TEST -001 ']"
    search_field_xpath = "//input[@type='search']"

    def checkbox(self):

        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@value = '21424']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value = '21424']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def order_out_for_delivery(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/orders/orderoutfordelivery/']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/orders/orderoutfordelivery/']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def move_to_delivered(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//a[contains(@class,'btn btn-block')])[2]"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class,'btn btn-block')])[2]"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def confirmation(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "(//button[text()='Yes'])[1]"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[text()='Yes'])[1]"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def carrier_name(self):
        self.send_value_to_element("carrier_name", self.carrier_name,
                                   ConfigReader.carrier_name(category, key))

    def shipment_document(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text() = 'Ship the Order']"))
        )

        verify_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text() = 'Ship the Order']"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(verify_btn).click().perform()

    def verify_company(self, branch_type_01):

        if branch_type_01 == 'NYB Distributors (Test) -- NYB Distributors - New York (Test)':
            print('pass')
        else:
            print('fail')
        return

    def search(self, category, key):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()



    def verify_add_products(self, expected_product_title, expected_flavor_title, expected_quantity_title):

        rows, doc_type = self.get_doc_type()

        product_title = []
        flavor_title = []
        quantity_title = []

        if rows is None:
            raise ValueError(f"Failed to retrieve rows for document type: {doc_type}")

        else:
            element_count = len(rows)
            for index in range(element_count):
                time.sleep(1)
                # Product.
                product = 0
                product_cell = rows[index].find_elements(By.TAG_NAME, 'td')[product]
                product_cell_val = product_cell.find_element(By.TAG_NAME, 'p')
                product_name = product_cell_val.text
                product_title.append(product_name)
                assert expected_product_title[index] == product_title[index]

                # Flavor.
                flavor = 1
                flavor_cell = rows[index].find_elements(By.TAG_NAME, 'td')[flavor]
                flavor_cell = flavor_cell.find_element(By.TAG_NAME, 'p')
                flavor_name = flavor_cell.text
                flavor_title.append(flavor_name)
                assert expected_flavor_title[index] == flavor_title[index]

                # Quantity (S/W).
                quantity = 2
                quantity_cell = rows[index].find_elements(By.TAG_NAME, 'td')[quantity]
                quantity_cell = quantity_cell.find_element(By.TAG_NAME, 'p')
                quantity_name = quantity_cell.text
                quantity_title.append(quantity_name)
                assert expected_quantity_title[index] == quantity_title[index]

        return product_title, flavor_title, quantity_title



    def get_doc_type(self):

        doc_type = self.get_element_text("document_type_id", self.document_type_id)
        rows = None
        if doc_type == "- | Xtend - Original - Italian Blood Orange - 30 Servings":
            rows = self.mul_elememts(
                "added_products_table_ps_xpath", self.added_products_table_ps_xpath)
        elif doc_type == "- | Xtend - Original - Smash Apple - 90 Servings":
            rows = self.mul_elememts(
                "added_products_table_vi_xpath", self.added_products_table_vi_xpath)
        elif doc_type == "- | Xtend - Original - Glacial Grape - 90 Servings":
            rows = self.mul_elememts(
                "added_products_table_it_xpath", self.added_products_table_it_xpath)
        elif doc_type == "- | Xtend - Original - Blue Raspberry Ice - 90 Servings":
            rows = self.mul_elememts(
                "added_products_table_pr_xpath", self.added_products_table_pr_xpath)
        elif doc_type == "- | Xtend - Original - Mango Madness - 90 Servings":
            rows = self.mul_elememts(
                "added_products_table_pr_xpath", self.added_products_table_pr_xpath)
        elif doc_type == "- | Xtend - Original - Strawberry Kiwi Splash - 90 Servings":
            rows = self.mul_elememts(
                "added_products_table_pr_xpath", self.added_products_table_pr_xpath)
        return rows, doc_type



    def document_type(self, doc_type):
        self.click_element("document_type_id", self.document_type_id)
        self.search1(doc_type)

    def verify_document_type(self, expected_doc_type):
        actual_doc_type = self.get_element_text("document_type_id", self.document_type_id)
        assert expected_doc_type == actual_doc_type
        return actual_doc_type

   # text = "//a[@href='/orders/orderreceived/21692/change/']"
    def verify_order_received(self, ):

        tc = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[@href='/orders/orderreceived/21692/change/']")))


        if tc == order_no_id:
            print('pass')
        else:
            print('fail')









