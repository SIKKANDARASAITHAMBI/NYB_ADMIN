import time

from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_by_locator_type(self, locator_type, locator_value):

        if locator_type.endswith('_xpath'):
            return self.driver.find_element(By.XPATH, locator_value)
        elif locator_type.endswith('_id'):
            return self.driver.find_element(By.ID, locator_value)
        elif locator_type.endswith('_name'):
            return self.driver.find_element(By.NAME, locator_value)
        elif locator_type.endswith('_classname'):
            return self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_type.endswith('_linktext'):
            return self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_type.endswith('_tagname'):
            return self.driver.find_element(By.TAG_NAME, locator_value)
        elif locator_type.endswith('_css'):
            return self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_type.endswith('_partial_link_text'):
            return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        else:
            raise ValueError(f"Unsupported locator type: {locator_type}")

    def click_element(self, locator_type, locator_value):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        element.click()

    def clear_element(self, locator_type, locator_value):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        element.clear()

    def send_value_to_element(self, locator_type, locator_value, send_text):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        element.send_keys(send_text)

    def locate_element(self, locator_type, locator_value):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        return element

    def get_element_text(self, locator_type, locator_value):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        return element.text

    def get_attribute_text(self, locator_type, locator_value, value):

        element = self.find_element_by_locator_type(locator_type, locator_value)
        return element.get_attribute(value)

    def get_page_url(self):

        return self.driver.current_url

    def mul_elememts(self, locator_type, locator_value):
        element = None

        if locator_type.endswith('_xpath'):
            element = self.driver.find_elements(By.XPATH, locator_value)

        elif locator_type.endswith('_id'):
            element = self.driver.find_elements(By.ID, locator_value)

        elif locator_type.endswith('_name'):
            element = self.driver.find_elements(By.NAME, locator_value)

        elif locator_type.endswith('_classname'):
            element = self.driver.find_elements(By.CLASS_NAME, locator_value)

        elif locator_type.endswith('_linktext'):
            element = self.driver.find_elements(By.LINK_TEXT, locator_value)

        elif locator_type.endswith('_tagname'):
            element = self.driver.find_elements(By.TAG_NAME, locator_value)

        elif locator_type.endswith('_css'):
            element = self.driver.find_elements(By.CSS_SELECTOR, locator_value)

        return element

    def scroll(self, element):

        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def screen_shot(self, save_location):

        self.driver.save_screenshot(save_location)

    def page_title(self):

        title = self.driver.title
        return title
