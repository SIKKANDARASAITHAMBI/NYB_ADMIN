import time

from selenium.webdriver import ActionChains, Keys

from features.pages.base_page import BasePage
import allure

from features.utilities import ConfigReader


class Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    success_message_xpath = "(//*[@class='success'])[1]"
    document_no_xpath = "(//input[@placeholder='Enter Document No. / No.'])"
    submit_btn_id = "submit-button"

    def get_success_message(self):
        doc_number_position = None
        success_message = self.get_element_text("success_message_xpath", self.success_message_xpath)
        if "vendor packing slip" in success_message:
            doc_number_position = 6
        elif "vendor invoice" in success_message or "purchase receipt" in success_message:
            doc_number_position = 5
        elif "intra-warehouse" in success_message:
            doc_number_position = 4
        else:
            raise ValueError("The success message does not contain any of the mentioned type")

        success_message_split = success_message.split()
        self.doc_number = success_message_split[doc_number_position]


    doc_type_xpath = "//*[@title='Select Document Type']"
    search_xpath = "//*[@type='search']"

    def search(self, category, key):
        search = self.locate_element("search_xpath", self.search_xpath)
        time.sleep(5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, ConfigReader.create_inbound_inventory(
            category, key))
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def filters(self, value):

        if value == "Document type":
            self.click_element("doc_type_xpath", self.doc_type_xpath)
            self.search("VALID INPUTS", "SOURCE_TYPE05")
        elif value == "Warehouse":
            pass
        elif value == "Vendors":
            pass
        elif value == "Document No":
            self.get_success_message()
            self.send_value_to_element("document_no_xpath", self.document_no_xpath, self.doc_number)
        self.click_element("submit_btn_id", self.submit_btn_id)

    def take_screen_shot(self, location):
        loc = location
        store_snap = self.screen_shot(loc)
        allure.attach(f"{store_snap}",
                      name="View Vendor Invoice", attachment_type=allure.attachment_type.PNG)


class VendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_xpath = "//table[@id='Event']//tbody//tr[1]//td"
    view_btn_xpath = "//table[@id='Event']//tbody//tr[1]//td[11]//a[text()='View']"
    no_xpath = "(//h5[@id ='exampleModalLongTitle'])[3]"
    vendor_packing_slip_details_xpath = \
        "(//table[@class='table table-bordered table-striped inward-items-list'])[1]//tbody//tr//td"
    items_xpath = "(//table[@id='Eventt'])[1]//tbody//tr"

    def listing(self):
        listings = self.mul_elememts("listing_xpath", self.listing_xpath)
        cell_count = len(listings)
        actual_listings = []
        for index in range(cell_count):
            cell_value = listings[index].text
            actual_listings.append(cell_value)
        actual_listings.pop()
        del actual_listings[0]
        allure.attach(f"{actual_listings}",
                      name="ACTUAL LISTING", attachment_type=allure.attachment_type.TEXT)
        return actual_listings

    def view_update_vendor_packing_slip(self, args):

        value = args[0]

        if value == "edit":
            pass
        elif value == "view":
            self.click_element("view_btn_xpath", self.view_btn_xpath)

            # The commented code is not needed now.
            '''
            Packing slip no.
            actual_no = self.get_element_text("no_xpath", self.no_xpath)
            actual_no = actual_no.split()
            actual_no = actual_no[2]
            expected_no = ConfigReader.create_inbound_inventory(category, no)
            allure.attach(f"{expected_no}",
                          name="EXPECTED PACKING SLIP NO.", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_no}",
                          name="Actual PACKING SLIP NO.", attachment_type=allure.attachment_type.TEXT)
            assert actual_no == expected_no
    
            #General Details.
            general_details = self.mul_elememts(
                "vendor_packing_slip_details_xpath", self.vendor_packing_slip_details_xpath)
            details_count = len(general_details)
            actual_details = []
            for index in range(details_count):
                if index % 2 != 0:
                    actual_details.append(general_details[index].text)
            allure.attach(f"{actual_details}",
                          name="Actual vendor packing slip details.", attachment_type=allure.attachment_type.TEXT)
            '''

            '''
             #ITEMS
            items = self.mul_elememts("items_xpath", self.items_xpath)
            items_count = len(items)
            for index in range(items_count-1):
                if index == 0:
                    pass
                if index == 1:
            '''
            loc = "C:/Users/Dell/LIFO PROJECTS/NYB ADMIN/features/configurations/Snaps/view_vendor_packing_slip.png"

            view_invoice = self.screen_shot(loc)
            allure.attach(f"{view_invoice}",
                          name="View Vendor Invoice", attachment_type=allure.attachment_type.PNG)

        elif value == "update_payment":
            pass

class VendorInvoice(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_row_xpath = "//table[@id='Event']//tbody//tr"

    def listing(self):

        listing_rows = self.mul_elememts("listing_row_xpath", self.listing_row_xpath)
        cell_count = len(listing_rows)
        assert cell_count == 1

    def view_update_vp_slip(self, value):

        if value == "edit":
            pass
        elif value == "view":
            #pass
            self.click_element("view_btn_xpath", self.view_btn_xpath)

        elif value == "update_payment":
            pass
        elif value == "create_invoice":
            pass

class IntraWareHouseTransfer(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def listing(self):
        pass

    def view_update_intrawarehouse_invoice(self, value):

        if value == "edit":
            pass
        elif value == "view":
            pass