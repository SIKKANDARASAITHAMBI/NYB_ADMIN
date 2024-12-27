import time
from lib2to3.fixes.fix_input import context

from selenium.common import exceptions, UnexpectedAlertPresentException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

from features.inventory.pages.base_page import BasePage
from features.inventory.utilities import ConfigReader


class CreateOrder(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search1(value):
        search = self.locate_element("search_field_xpath", self.search_field_xpath)
        time.sleep(0.5)
        actions = ActionChains(self.driver)
        actions.send_keys_to_element(search, value)
        actions.send_keys(Keys.ENTER)
        actions.perform()
