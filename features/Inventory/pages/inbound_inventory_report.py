import allure

from features.Inventory.pages.base_page import BasePage


class inbound_inventory_report(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def take_screen_shot(self, location):
        loc = location
        store_snap = self.screen_shot(loc)
        allure.attach(f"{store_snap}",
                      name="View Vendor Packing Slip In Inbound Inventory Report",
                      attachment_type=allure.attachment_type.PNG)