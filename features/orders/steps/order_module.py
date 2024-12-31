import configparser
import os
import time

import allure
from behave import *

from features.orders.pages.url_verification import UrlVerification
from features.orders.pages.order import HeaderNavigators
from features.orders.utilities import ConfigReader
from features.orders.pages.create_order import CreateOrder

exist_product_01 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME01")
exist_product_02 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME02")
exist_product_03 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME03")
exist_product_04 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME04")
exist_product_05 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME05")
exist_product_06 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME06")


branch_type_01 = ConfigReader.create_order("VALID_INPUTS", "branch_type1")
payment_type_01 = ConfigReader.create_order("VALID_INPUTS", "PAYMENT_MODE1")
@when(u'I navigate to the Order module and verified the landing page URL,')
def inventory_nav(context):
    context.hn = HeaderNavigators(context.driver)
    context.hn.header_navs("order")
    context.url = UrlVerification(context.driver)
    context.url.order_urls()

    # with allure.step(f"Navigating to the inventory module > Create Inbound Inventory page"):
    #     try:
    #         context.hn = HeaderNavigators(context.driver)
    #         context.hn.header_navs("order")
    #         allure.attach(context.driver.get_screenshot_as_png(), name="Order page navigation successfull",
    #                       attachment_type=allure.attachment_type.PNG)
    #     except Exception as e:
    #         allure.attach(context.driver.get_screenshot_as_png(), name="Order page navigation unsuccessfull",
    #                       attachment_type=allure.attachment_type.PNG)
    #         raise Exception(f"Error during login: {e}")
    # with allure.step(f"Verify the landing page Url"):
        # try:
        #     context.url = UrlVerification(context.driver)
        #     expected_url, actual_url = context.url.order_urls()
        #     allure.attach(f"{expected_url}",
        #                   name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
        #     allure.attach(f"{actual_url}",
        #                   name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)
        # except Exception as e:
        #     allure.attach(f"{expected_url}",
        #                   name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
        #     allure.attach(f"{actual_url}",
        #                   name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)

@when(u'I choose the company/branch type, shipping address, order date,')
def company(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateOrder(context.driver)
    context.cvp.branch(branch_type_01)





'''
    with allure.step(f"{branch_type_01} selected as branch type"):
        try:
            context.cvp.branch_type1(branch_type_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Branch type selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Branch type selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting branch type '{branch_type_01}': {e}")

'''

@when(u'I add Products,')
def add_products(context):

    with allure.step(f"""added products
                        Product1: {exist_product_01},
                        Product2: {exist_product_02},
                        Product3: {exist_product_03},
                        Product4: {exist_product_04},
                        Product5: {exist_product_05},
                        Product6: {exist_product_06}"""):
        try:
            product_data = [exist_product_01, exist_product_02, exist_product_03, exist_product_04, exist_product_05,
                            exist_product_06]
            context.cvp.add_products(product_data)
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding Products. is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding Products. is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"""Error Adding Products: 
                                product1: {exist_product_01},
                                product2: {exist_product_02},
                                product3: {exist_product_03},
                                product4: {exist_product_04},
                                product5: {exist_product_05},
                                product6: {exist_product_06},:""" f"{e}")

@then(u'I select Payment Mode,')
def payment_mode(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateOrder(context.driver)
    context.cvp.payment(payment_type_01)

@then(u'I click Submit Order,')
def submit_order(context):
    with allure.step(f"Submit button clicked"):
        try:
            context.cvp.submit_order()
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking submit button: {e}")

@then(u'I Verify account name to submit order,')
def Verify_account_name(context):
    with allure.step(f"Yes is clicked"):
        try:
            context.cvp.Verify_account()
            allure.attach(context.driver.get_screenshot_as_png(), name="Verify account successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Verify account unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking submit button: {e}")

@then(u'I verify the Order Received landing page URL,')
def verify_order(context):
    with allure.step(f" Verify the landing page Url"):
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


@then(u'I verify the Order placed success message,')
def Order_Placed_msg(context):
    with allure.step(f"Ok is clicked"):
        try:
            context.cvp.Verify_Order_Placed()
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking order placed: {e}")


@then(u'I Enter Order ID,')
def Order_ID(context):
    context.driver.implicitly_wait(20)
    (context.cvp.order_no("VALID_INPUTS", "ORDER_ID"))

@when(u'I click Order Received Page,')
def Order_Received_Page(context):
    with allure.step(f"Order Received Page is clicked"):
        try:
            context.cvp.Order_Received_Page()
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking Order Received Page: {e}")