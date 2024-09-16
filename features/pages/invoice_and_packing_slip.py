import time
from datetime import datetime
from features.pages.base_page import BasePage
from features.utilities import ConfigReader
import allure


class VendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_xpath = "//table[@id='Event']//tbody//tr[1]//td"
    view_btn_xpath = "//table[@id='Event']//tbody//tr[1]//td[11]//a[2]"
    no_xpath = "(//h5[@id ='exampleModalLongTitle'])[3]"
    vendor_packing_slip_details_xpath = \
        "(//table[@class='table table-bordered table-striped inward-items-list'])[1]//tbody//tr//td"

    def listing(self):
        listings = self.mul_elememts("listing_xpath",self.listing_xpath)
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
    def view(self):
        self.click_element("view_btn_xpath", self.view_btn_xpath)

    def verify_view_details(self, category, no):

        #Packing slip no.
        actual_no = self.get_element_text("no_xpath", self.no_xpath)
        actual_no = actual_no.split()
        actual_no = actual_no[2]
        expected_no = ConfigReader.create_inbound_inventory(category, no)
        allure.attach(f"{expected_no}",
                      name="EXPECTED PACKING SLIP NO.", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"{actual_no}",
                      name="Actual PACKING SLIP NO.", attachment_type=allure.attachment_type.TEXT)
        assert actual_no == expected_no

        #Warehouse.
        general_details = self.mul_elememts(
            "vendor_packing_slip_details_xpath", self.vendor_packing_slip_details_xpath)
        details_count = len(general_details)
        actual_details = []
        for index in range(details_count):
            if index % 2 != 0:
                actual_details.append(general_details[index].text)
        allure.attach(f"{actual_details}",
                      name="Actual vendor packing slip details.", attachment_type=allure.attachment_type.TEXT)