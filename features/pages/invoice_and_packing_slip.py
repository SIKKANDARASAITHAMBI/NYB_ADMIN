import time
from datetime import datetime
from features.pages.base_page import BasePage
from features.utilities import ConfigReader
import allure


class Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
    success_message_xpath = "(//*[@class='success'])[1]"
    document_no_xpath = "(//input[@placeholder='Enter Document No. / No.'])"
    submit_btn_id = "submit-button"

    def get_success_message(self):
        success_message = self.get_element_text("success_message_xpath", self.success_message_xpath)
        success_message = success_message.split()
        self.doc_number = success_message[6]

    def filters(self, args):
        value = args
        if value == "document_type":
            pass
        elif value == "warehouse":
            pass
        elif value == "vendors":
            pass
        elif value == "document_no":
            success_txt = self.get_success_message()
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

    def listing(self):
        pass

    def view_update_vp_slip(self, value):

        if value == "edit":
            pass
        elif value == "view":
            pass
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