from features.pages.base_page import BasePage


class HeaderNavigators(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    inventory_nav_xpath = "//a[@href='/inventory/createinward/']"
    invoice_and_packing_slips_nav_xpath = "//a[@href='/inventory/vendorpackingslip/']"
    onhand_inventory_nav_linktext = "3.On Hand Inventory "
    inbound_inventory_report_nav_linktext = "4.Inbound Inventory Report"
    inventory_moment_report_nav_linktext = "5.Inventory movement Report"

    def header_navs(self, page):
        if page == "inventory":
            self.click_element(
                "inventory_nav_xpath", self.inventory_nav_xpath)
        elif page == "invoice and packingslip":
            self.click_element(
                "invoice_and_packing_slips_nav_xpath", self.invoice_and_packing_slips_nav_xpath)
        elif page == "On hand inventory":
            self.click_element(
                "onhand_inventory_nav_linktext", self.onhand_inventory_nav_linktext)
        elif page == "inbound inventory report":
            self.click_element(
                "inbound_inventory_report_nav_linktext", self.inbound_inventory_report_nav_linktext)
        elif page == "inventory moment report nav linktex":
            self.click_element(
                "inventory_moment_report_nav_linktext", self.inventory_moment_report_nav_linktext)