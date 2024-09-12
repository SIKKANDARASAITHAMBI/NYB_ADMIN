from datetime import datetime
from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class VendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_xpath = "//table[@id='Event']//tbody//tr[1]//td"
    view_btn_xpath = "//table[@id='Event']//tbody//tr[1]//td[11]//a[2]"
    no_xpath = "(//h5[@id ='exampleModalLongTitle'])[5]"

    def listing(self):
        listings = self.mul_elememts("listing_xpath",self.listing_xpath)
        cell_count = len(listings)
        actual_listings = []
        for index in range(cell_count):
            cell_value = listings[index].text
            actual_listings.append(cell_value)
        actual_listings.pop()
        del actual_listings[0]
        return actual_listings

    def view(self):
        self.click_element("view_btn_xpath", self.view_btn_xpath)

    def verify_view_details(self, *args):
        #Packing slip no.
        actual_no = self.get_element_text("no_xpath", self.no_xpath)
        actual_no = actual_no.split()
        actual_no = actual_no[2]
        category = args
        no = args
        expected_no = ConfigReader.create_inbound_inventory(category, no)
        assert actual_no == expected_no

        #Warehouse.
