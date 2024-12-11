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

from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class CreateVendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    document_type_id = "select2-source_id-container"
    document_type_xpath = "//*[@id='select2-source_id-container']"
    search_field_xpath = "//input[@type='search']"
    search2_field_xpath = "//input[@role='searchbox']"
    warehouse_field_id = "select2-warehouse_id-container"
    vendor_field_id = "select2-supplier_id-container"
    from_warehouse_xpath = "(//span[@role='textbox'])[2]"
    to_warehouse_xpath = "(//span[@role='textbox'])[3]"
    packing_slip_no_id = "packing_slip"
    packing_slip_date_id = "packing_slip_date"
    packing_slip_received_date_id = "packing_slip_received_date"
    purchase_order_no_id = "purchase_order_no"
    vendor_invoice_no_id = "supplier_invoice_no"

    purchase_order_date_id = "purchase_order_date"
    payment_receipt_no_id = "supplier_invoice_no"
    # payment_mode_xpath = "//label[@for='company_id']/following-sibling::select[1]/option[2]"
    packing_slip_upload = "packing_slip_upload"
    discounts_id = "discount"
    document_proof_id = "document_proof_id"
    tax_id = "tax"
    other_charges_id = "other_charges_id"
    notes_id = "notes"
    upload_invoice = "upload_invoice"
    upload_transfer_invoice = "transfer_slip_upload"
    transfer_no_xpath = "(//input[contains(@class,'packing_slip form-control')])[2]"
    Replacement_for_damaged_items_xpath = "//span[text()='Replacement for Damaged Items']"
    order_id = "select2-order_id-container"
    Payment_Reciept = "select2-source_id-container"
    add_product_field_id = "select2-product_id-container"
    add_sample_product_field_id = "select2-product_dropdown-container"
    sample_product_check_box_xpath = "(//table[contains(@class,'table table-striped')]/following::table)[5]/tbody[1]/tr[1]/td[1]/input[1]"
    sample_product_name_xpath = "(//table[@CLASS='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr//td[2]"

    sample_flavor_name_xpath = "(//table[@CLASS='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr//td[3]"
    sample_size_weight_variant_name_xpath = "(//table[@CLASS='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr//td[4]"
    sample_product_price_field_xpath = "(//table[@CLASS='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr//td[5]"
    confirm_btn_id = "confirmButton"
    added_products_table_ps_xpath = "//table[@id='tblpackingslip']//tbody[@id='packingtbody']//tr"
    added_products_table_it_xpath = "//table[@id='tbltransferslip']//tbody[@id='transfertbody']//tr"
    inward_qty_xpath = "td"
    damaged_qty_xpath = "td"
    unit_price_xpath = "td"
    batch_no_xpath = "td"
    expiry_date_xpath = "td"
    product_name_xpath = "select2-search__field"
    flavor_xpath = "td"
    size_weight_xpath = "td"
    price_xpath = "td"
    product_name_name_xpath = "product_name_name_xpath = '//input[@class='form-control newProductText']'"
    submit_btn_xpath = "//button[text()='Submit']"
    click_random_xpath = "(//*[@class='form-row'])"
    add_product_xpath = "(//*[text()='Add New Product'])[2]"
    add_new_product_xpath = "//select//option[text() = 'Add New Product']"
    add_new_table_pd_xpath = "(//table[contains(@class,'table table-striped')]/following::table)[5]/tbody[1]/tr[1]/td[2]"
    sample_table_xpath = "(//table[@class='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr"
    sample_table_xpath_enter = "((//table[@class='table table-striped table-bordered table-hover table-heading no-border-bottom'])[5]//tbody//tr//input)"
    added_products_table_vi_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"
    added_products_table_rd_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"
    added_products_table_pr_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"
    sp1_added_products_table_vi_xpath = "//h5[text()='New Products / New Flavors / Samples / Brand Promo Items (Merchandise, Sippers etc.)']"
    sp2_added_products_table_vi_xpath = "//span[@id='select2-product_dropdown-container']/following-sibling::span[1]"
    sp3_added_products_table_vi_xpath = "(//tbody[@id='productTableBody']//label)[2]"
    sp4_added_products_table_vi_xpath = "(//input[@type='checkbox'])[2]"
    add_newest_product_xpath = "//input[@placeholder='Enter Product Name']"

    def search(self, category, key):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def search1(self, value):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, value)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def document_type(self, category, key):
        self.click_element("document_type_id", self.document_type_id)
        self.search(category, key)

    def warehouse(self, category, key):
        self.click_element("warehouse_field_id", self.warehouse_field_id)
        self.search(category, key)

    payment_mode_id = "payment_mode"

    def search2(self, category, key):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "search2_field_xpath"))
        )

        search2_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "search2_field_xpath"))
        )
        actions = ActionChains(self.driver)
        actions.move_to_element(search2_btn).click().perform()

    def payment_mode(self, category, key):

        payment_mode_field = (self.locate_element("payment_mode_id", self.payment_mode_id))
        select = Select(payment_mode_field)
        payment_mode = ConfigReader.create_inbound_inventory(category, key)
        if payment_mode == "check":
            select.select_by_value("check")
        else:
            select.select_by_value("credit_card")

    def vendors(self, category, key):
        self.click_element("vendor_field_id", self.vendor_field_id)
        self.search(category, key)

    vendor_name_id = "vendor_name"

    def vendor_name(self, category, key):
        vendor_name = ConfigReader.create_inbound_inventory(category, key)
        self.send_value_to_element("vendor_name_id", self.vendor_name_id, vendor_name)

    def from_warehouse(self, category, key):
        self.click_element("from_warehouse_xpath", self.from_warehouse_xpath)
        self.search(category, key)

    def to_warehouse(self, category, key):
        self.click_element("to_warehouse_xpath", self.to_warehouse_xpath)
        self.search(category, key)

    def pk_no(self, category, key):
        self.send_value_to_element("packing_slip_no_id", self.packing_slip_no_id,
                                   ConfigReader.create_inbound_inventory(category, key))

    def intra_ware_house_transfer_no(self, category, key):
        self.send_value_to_element("transfer_no_xpath", self.transfer_no_xpath,
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

    def vendor_invoice_no(self, category, vendor_invoice_no):
        self.clear_element("vendor_invoice_no_id", self.vendor_invoice_no_id)
        self.send_value_to_element(
            "vendor_invoice_no_id", self.vendor_invoice_no_id,
            ConfigReader.create_inbound_inventory(
                category, vendor_invoice_no))

    def purchase_order_no(self, category, purchase_order_no):
        self.clear_element("purchase_order_no_id", self.purchase_order_no_id)
        self.send_value_to_element(
            "purchase_order_no_id", self.purchase_order_no_id,
            ConfigReader.create_inbound_inventory(
                category, purchase_order_no))

    def payment_receipt_no(self, category, payment_receipt_no):

        self.send_value_to_element(
            "payment_receipt_no_id", self.payment_receipt_no_id,
            ConfigReader.create_inbound_inventory(
                category, payment_receipt_no))

    def discounts(self, category, discounts):
        self.clear_element("discounts_id", self.discounts_id)
        self.send_value_to_element(
            "discounts_id", self.discounts_id,
            ConfigReader.create_inbound_inventory(
                category, discounts))

    def tax(self, category, tax):
        self.clear_element("tax_id", self.tax_id)
        self.send_value_to_element(
            "tax_id", self.tax_id,
            ConfigReader.create_inbound_inventory(
                category, tax))

    def other_charges(self, category, other_charges):
        self.clear_element("other_charges_id", self.other_charges_id)
        self.send_value_to_element(
            "other_charges_id", self.other_charges_id,
            ConfigReader.create_inbound_inventory(
                category, other_charges))

    def notes(self, category, notes):
        self.clear_element("notes_id", self.notes_id)
        self.send_value_to_element(
            "notes_id", self.notes_id,
            ConfigReader.create_inbound_inventory(
                category, notes))

    def purchase_order_date(self, category, purchase_order_date):
        self.clear_element("purchase_order_date_id", self.purchase_order_date_id)
        self.send_value_to_element(
            "purchase_order_date_id", self.purchase_order_date_id,
            ConfigReader.create_inbound_inventory(
                category, purchase_order_date))
        self.click_element("click_random_xpath", self.click_random_xpath)

    def upload_packing_slip(self, file_path):
        file_input = self.driver.find_element(By.ID, 'packing_slip_upload')
        file_input.send_keys(file_path)

    def upload_invoicee(self, file_path):
        file_input = self.driver.find_element(By.ID, 'upload_invoice')
        file_input.send_keys(file_path)

    def upload_transfer_invoices(self, file_path):
        file_input = self.driver.find_element(By.ID, 'transfer_slip_upload')
        file_input.send_keys(file_path)

    def document_proof_ids(self, file_path):
        file_input = self.driver.find_element(By.ID, 'document_proof_id')
        file_input.send_keys(file_path)

    def add_products(self, category, products):
        self.click_element("add_product_field_id", self.add_product_field_id)
        self.search(category, products)
        # self.search("VALID INPUTS", "")

        time.sleep(1)

    product_li_xpath = "//li[@class='select2-results__option select2-results__option--selectable']"

    def add_sample_products(self, value: list):
        products_count = len(value)
        for index in range(products_count):
            time.sleep(1)
            self.click_element("add_sample_product_field_id", self.add_sample_product_field_id)
            self.search1(value[index])
        # list_products = self.mul_elememts("product_li_xpath", self.product_li_xpath)
        # for product in list_products:
        #     product_name = product.text
        #     if product_name == "Add New Product":
        #         product.click()
        #         break

    def is_sample_product(self):
        self.click_element(
            "sample_product_check_box_xpath", self.sample_product_check_box_xpath)

    # NEED TO WORK HERE#

    #def sample_product_name(self, category, sample_product_name):
    #self.send_value_to_element(
    #  "sample_product_name_xpath", self.sample_product_name_xpath,
    #  ConfigReader.create_inbound_inventory(category, sample_product_name))

    get_products_xpath = "//li[@class='select2-results__option select2-results__option--selectable']"

    def sample_product_name(self, category, key):
        products_list = self.mul_elememts("sample_product_name_xpath", self.sample_product_name_xpath)
        for product_list in products_list:
            product_name = product_list.text
            if product_name == sample_product:
                product_list.click()
                break
                time.sleep(10)

    def sample_products_flavor_name(self, category, key):
        self.click_element("sample_flavor_name_xpath", self.sample_flavor_name_xpath)
        time.sleep(5)
        self.search(category, key)

    def sample_product_flavors_size_weight_variant_name(self, category, key):
        self.click_element("sample_size_weight_variant_name_xpath", self.sample_size_weight_variant_name_xpath)
        time.sleep(5)
        self.search(category, key)

    def sample_product_price(self, category, key):

        #self.click_element("sample_product_price_field_xpath", self.sample_product_price_field_xpath)
        search = self.locate_element("sample_product_price_field_xpath", self.sample_product_price_field_xpath)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()
        # time.sleep(1)

    def confirm(self):
        self.click_element("confirm_btn_id", self.confirm_btn_id)

    # Static Code.

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
    def table(self, category, inward_quantity, damaged_quantity, unit_price, batch_number,
              expiry_date):
        doc_type = self.get_element_text("document_type_xpath", self.document_type_xpath)
        rows = None
        if doc_type == "Vendor Packing Slip":
            rows = self.mul_elememts(
                "added_products_table_ps_xpath", self.added_products_table_ps_xpath)
        elif doc_type == "Vendor Invoice":
            rows = self.mul_elememts(
                "added_products_table_vi_xpath", self.added_products_table_vi_xpath)
        elif doc_type == "IntrawarehouseTransfer Invoice":
            rows = self.mul_elememts(
                "added_products_table_it_xpath", self.added_products_table_it_xpath)
        elif doc_type == "Payment Receipt":
            rows = self.mul_elememts(
                "added_products_table_pr_xpath", self.added_products_table_pr_xpath)
        if rows is None:
            raise ValueError(f"Failed to retrieve rows for document type: {doc_type}")
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

    def sample_product_table(self, is_sample, product, flavor, quantity, price):

        add_products = self.get_element_text(
            "add_new_product_xpath", self.add_new_product_xpath)

        rows = None
        if add_products == "Add New Product":
            rows = self.mul_elememts("sample_table_xpath", self.sample_table_xpath)
            print(len(rows))

        if rows is None:
            raise ValueError(f"Failed to retrieve rows for document type: {add_products}")

        element_count = len(rows)

        for index in range(element_count):
            time.sleep(3)

            # Is Sample Product Check Box
            if is_sample[index] is True:
                is_sample_cb_index = 0
                is_sample_cb_element = rows[index].find_elements(By.TAG_NAME, 'td')[is_sample_cb_index]
                is_sample_cb_element.click()

            # Add New Product
            product_index = 1
            product_element = rows[index].find_elements(By.TAG_NAME, 'td')[product_index]
            product_element.click()
            try:
                self.search1(product[index])
            except NoSuchElementException:
                pass

            if product[index] == "Add New Product":
                try:
                    new_product_name = product_element.find_element(By.TAG_NAME, "input")
                    new_product_name.send_keys("Sample Test product")
                except NoSuchElementException:
                    pass

            """
            If the search field is not working in the dropdown use the following code. 
            
            pdt_list = "//li[@class='select2-results__option select2-results__option--selectable']"
            
            list_products1 = self.mul_elememts("pdt_list", self.pdt_list)
            print(len(list_products1))
            print(list_products1)
            for product1 in list_products1:
                product_name1 = product1.text
                if product_name1 == "Add New Product":
                    product1.click()
                    break
            """

            # Add New Flavor
            flavor_index = 2
            flavor_element = rows[index].find_elements(By.TAG_NAME, 'td')[flavor_index]
            flavor_element.click()
            try:
                self.search1(flavor[index])
            except NoSuchElementException:
                pass

            if flavor[index] == "Add New Flavor":
                try:
                    new_flavor_input_field = flavor_element.find_element(By.TAG_NAME, "input")
                    new_flavor_input_field.send_keys("Sample Test Flavor")
                except NoSuchElementException:
                    pass

            # Add New Flavor
            quantity_index = 3
            quantity_element = rows[index].find_elements(By.TAG_NAME, 'td')[quantity_index]
            quantity_element.click()
            try:
                self.search1(quantity[index])
            except NoSuchElementException:
                pass

            if quantity[index] == "Add New Size/Weight":
                try:
                    new_quantity_input_field = quantity_element.find_element(By.TAG_NAME, "input")
                    new_quantity_input_field.send_keys("Sample Test quantity")
                except NoSuchElementException:
                    pass

            price_index = 4
            price_element = rows[index].find_elements(By.TAG_NAME, 'td')[price_index]
            price_input_field = price_element.find_element(By.TAG_NAME, 'input')
            price_input_field.send_keys(price[index])

    def sample_product_table_existing_combo(self, is_sample):

        add_products = self.get_element_text(
            "add_new_product_xpath", self.add_new_product_xpath)

        rows = None
        if add_products == "Add New Product":
            rows = self.mul_elememts("sample_table_xpath", self.sample_table_xpath)
            print(len(rows))

        if rows is None:
            raise ValueError(f"Failed to retrieve rows for document type: {add_products}")

        element_count = len(rows)

        for index in range(element_count):
            time.sleep(1)

            # Is Sample Product Check Box
            if is_sample[index] is True:
                is_sample_cb_index = 0
                is_sample_cb_element = rows[index].find_elements(By.TAG_NAME, 'td')[is_sample_cb_index]
                is_sample_cb_element.click()
