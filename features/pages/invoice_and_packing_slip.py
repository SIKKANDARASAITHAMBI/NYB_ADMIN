import time

from features.pages.base_page import BasePage


class VendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_xpath = "//table[@id='Event']//tbody//tr[1]//td"
    view_btn_xpath = "//table[@id='Event']//tbody//tr[1]//td[11]//a[2]"

    def listing(self):
        listings = self.mul_elememts("listing_xpath",self.listing_xpath)
        cell_count = len(listings)
        actual_listings = []
        for index in range(cell_count):
            cell_value = listings[index].text
            actual_listings.append(cell_value)
        actual_listings.pop()
        del actual_listings[0]
        print(f"Actual Listing Values:{actual_listings}")

    def view(self):
        self.click_element("view_btn_xpath", self.view_btn_xpath)

    def verify_view_details(self):
        pass