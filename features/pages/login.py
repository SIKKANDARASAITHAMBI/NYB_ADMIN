from features.pages.base_page import BasePage
from features.utilities import ConfigReader


class Login(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    username_id = "id_username"
    password_id = "id_password"
    login_btn_xpath = "//*[@value='Log in']"

    def login_form(self, category, username, password):
        self.send_value_to_element(
            "username_id", self.username_id, ConfigReader.login(
                category, username))
        self.send_value_to_element(
            "password_id", self.password_id, ConfigReader.login(
                category, password))
        self.click_element("submit_btn_xpath", self.login_btn_xpath)
