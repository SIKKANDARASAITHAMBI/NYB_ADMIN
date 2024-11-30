import time
from lib2to3.fixes.fix_input import context

from selenium.webdriver import ActionChains, Keys
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
    search_field_xpath = "//input[@type='search']"
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
    sample_product_check_box_xpath = "//table//tbody//td//input[@type='checkbox']"
    sample_product_name_xpath = "//table//tbody//td//input[@placeholder='Enter Product Name']"
    sample_flavor_name_xpath = "//table//tbody//td//input[@placeholder='Enter Flavor Name']"
    sample_size_weight_variant_name_xpath = "//table//tbody//td//input[@placeholder='Enter Size/Weight']"
    sample_product_price_field_xpath = "//table//tbody//td//input[@placeholder='Enter Price']"
    confirm_btn_id = "confirmButton"
    added_products_table_ps_xpath = "//table[@id='tblpackingslip']//tbody[@id='packingtbody']//tr"
    added_products_table_it_xpath = "//table[@id='tbltransferslip']//tbody[@id='transfertbody']//tr"
    inward_qty_xpath = "td"
    damaged_qty_xpath = "td"
    unit_price_xpath = "td"
    batch_no_xpath = "td"
    expiry_date_xpath = "td"
    submit_btn_xpath = "//button[text()='Submit']"
    click_random_xpath = "(//*[@class='form-row'])"
    add_product_xpath = "(//*[text()='Add New Product'])[2]"
    added_products_table_vi_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"
    added_products_table_rd_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"
    added_products_table_pr_xpath = "//table[@id='tblproduct']//tbody[@id='tblbody']//tr"


    def search(self, category, key):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(0.5)
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

    payment_mode_id = "payment_mode"

    def payment_mode(self,category, key):

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

    def from_warehouse(self, category, key):
        self.click_element("from_warehouse_xpath", self.from_warehouse_xpath)
        self.search(category, key)

    def to_warehouse(self, category, key):
        self.click_element("to_warehouse_xpath", self.to_warehouse_xpath)
        self.search(category, key)

    def order_ids(self, category, key):
        self.click_element("order_id", self.order_id)
        self.search(category, key)


    def no(self, category, key):
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
        self.clear_element("payment_receipt_no_id", self.payment_receipt_no_id)
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

    def upload_packing_slip(self):
        file_input = self.driver.find_element(By.ID, 'packing_slip_upload')
        file_path = "C:/Users/hp/Desktop/nyb.PNG"
        file_input.send_keys(file_path)

    def upload_the_invoice(self):
        file_input = self.driver.find_element(By.ID, 'upload_invoice')
        file_path = "C:/Users/sikku/Downloads/Woodbolt_Distribution_cellucor_Packing_slip_11_27_2024.pdf"
        file_input.send_keys(file_path)

    def upload_transfer_invoices(self):
        file_input = self.driver.find_element(By.ID, 'transfer_slip_upload')
        file_path = "C:/Users/hp/Desktop/nyb.PNG"
        file_input.send_keys(file_path)

    def document_proof_ids(self):
        file_input = self.driver.find_element(By.ID, 'document_proof_id')
        file_path = "C:/Users/hp/Desktop/nyb.PNG"
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
    def table(self, category, inward_quantity, damaged_quantity, unit_price, batch_number,
                                  expiry_date, doc_type):
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
        elif doc_type == "Replacement_for_damaged_items":
            rows = self.mul_elememts(
                "added_products_table_rd_xpath", self.added_products_table_rd_xpath)
        elif doc_type == "Payment Receipt":
            rows = self.mul_elememts(
                "added_products_table_pr_xpath", self.added_products_table_pr_xpath)


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





