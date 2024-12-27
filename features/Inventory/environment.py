import configparser
import logging
from selenium import webdriver

from features.Inventory.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.Inventory.pages.invoice_and_packing_slip import VendorInvoice, Page
from features.Inventory.utilities import ConfigReader

executable_browser = ConfigReader.basic_info("BASIC INFO", "BROWSER_NAME_01")


def before_scenario(context, driver):
    logging.basicConfig(level=logging.DEBUG)

    if executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_01"):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
    elif executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_02"):
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()
    elif executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_03"):
        context.driver = webdriver.Edge()
        context.driver.maximize_window()
    else:
        raise ValueError("Unsupported browser specified in the configuration file")

    context.driver.implicitly_wait(10)

    #Object initializatation
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.page = Page(context.driver)
    context.vi = VendorInvoice(context.driver)



def after_scenario(context, driver):
    context.driver.quit()