import configparser
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service

from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.invoice_and_packing_slip import Page, VendorInvoice
from features.utilities import ConfigReader

executable_browser = ConfigReader.basic_info("BASIC INFO", "BROWSER_NAME_01")


def before_scenario(context, driver):
    logging.basicConfig(level=logging.DEBUG)
    service_obj = Service()
    if executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_01"):
        context.driver = webdriver.Chrome(service=service_obj)
        context.driver.maximize_window()
    elif executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_02"):
        context.driver = (webdriver.Firefox(service=service_obj))
        context.driver.maximize_window()
    elif executable_browser == ConfigReader.expected_outcome("EXPECTED OUTCOME", "BROWSER_NAME_03"):
        context.driver = (webdriver.Edge(service=service_obj))
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