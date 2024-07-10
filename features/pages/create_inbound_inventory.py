from features.pages.base_page import BasePage


class CreateInBoundInventory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    document_type_id = "select2-source_id-container"
    search_field_xpath = "//*[@type='search']"

    def create_vendor_packing_slip_valid_inputs(self):
        self.click_element("document_type_id", self.document_type_id)
        self.send_value_to_element("search_field_xpath", self.search_field_xpath, )
