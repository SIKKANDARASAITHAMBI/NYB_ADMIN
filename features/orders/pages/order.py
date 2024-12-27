from features.Inventory.pages.base_page import BasePage


class HeaderNavigators(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    order_nav_xpath = "//a[@href='/orders/createorder/']"

    def header_navs(self, page):
        if page == "order":
            self.click_element(
                "order_nav_xpath", self.order_nav_xpath)

