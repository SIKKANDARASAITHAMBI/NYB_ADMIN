from features.pages.base_page import BasePage


class HeaderNavigators(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    inventory_nav_xpath = "//a[@href='/inventory/createinward/']"
    invoice_and_packing_slips_nav_xpath = "//a[@href='/inventory/vendorpackingslip/']"


    def inventory(self):
        self.click_element("inventory_nav_xpath", self.inventory_nav_xpath)

    def invoice_and_packingslip(self):
        self.click_element("invoice_and_packing_slips_nav_xpath", self.invoice_and_packing_slips_nav_xpath)