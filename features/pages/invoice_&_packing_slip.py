from features.pages.base_page import BasePage


class VendorPackingSlip(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    listing_xpath = "//table[@id='Event']//tbody//tr[1]//td"

    def listing(self):
        listings = self.mul_elememts("listing_xpath",self.listing_xpath)
        cell_count = len(listings)
        actual_listings = []
        for index in range(cell_count[1:]):
            cell_value = self.get_element_text("listing_xpath",self.listing_xpath)
            cell_value = cell_value[index]
            actual_listings.append(cell_value)
        print(actual_listings)
        a = 10
        b = 15
        assert a == b