import configparser
import os
import time

import allure
from behave import *

from features.Inventory.pages.url_verification import UrlVerification
from features.orders.pages.order import HeaderNavigators


@when(u'I navigate to the Order module and verified the landing page URL,')
def inventory_nav(context):
    with allure.step(f"Navigating to the inventory module > Create Inbound Inventory page"):
        try:
            context.hn = HeaderNavigators(context.driver)
            context.hn.header_navs("order")
            allure.attach(context.driver.get_screenshot_as_png(), name="Order page navigation successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order page navigation unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error during login: {e}")
        with allure.step(f"Verify the landing page Url"):
            try:
                context.url = UrlVerification(context.driver)
                expected_url, actual_url = context.url.order_urls()
                allure.attach(f"{expected_url}",
                              name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
                allure.attach(f"{actual_url}",
                              name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)
            except Exception as e:
                allure.attach(f"{expected_url}",
                              name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
                allure.attach(f"{actual_url}",
                              name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)
