import configparser
import os
import time

import allure
from behave import *

from features.orders.pages.url_verification import UrlVerification
from features.orders.pages.order import HeaderNavigators
from features.orders.utilities import ConfigReader
from features.orders.pages.create_order import CreateOrder
#from features.orders.configurations.basic_info.ini import webdriver

exist_product_01 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME01")
exist_product_02 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME02")
exist_product_03 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME03")
exist_product_04 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME04")
exist_product_05 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME05")
exist_product_06 = ConfigReader.create_order("VALID_INPUTS", "PRODUCT_NAME06")


branch_type_01 = ConfigReader.create_order("VALID_INPUTS", "branch_type1")
payment_type_01 = ConfigReader.create_order("VALID_INPUTS", "PAYMENT_MODE2")


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

@then(u'I Verify the company/branch type, shipping address, order date,')
def verify_company(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateOrder(context.driver)
    context.cvp.verify_company(branch_type_01)


'''
@then(u'I verify Products,')
def verify_added_products(context):

    concatenated_list = []
    prod_06 = exist_product_06.split(" - ")
    prod_05 = exist_product_05.split(" - ")
    prod_04 = exist_product_04.split(" - ")
    prod_03 = exist_product_03.split(" - ")
    prod_02 = exist_product_02.split(" - ")
    prod_01 = exist_product_01.split(" - ")

    expected_product_titles = [prod_06[0], prod_05[0], prod_04[0],
                               prod_03[0], prod_02[0], prod_01[0]]

    expected_flavor_titles = [prod_06[1], prod_05[1], prod_04[1],
                              prod_03[1], prod_02[1], prod_01[1]]

    expected_quantity_titles = [prod_06[2], prod_05[2], prod_04[2],
                                prod_03[2], prod_02[2], prod_01[2]]

    product_title, flavor_title, quantity_title = context.cvp.verify_add_products(
        expected_product_titles, expected_flavor_titles,
        expected_quantity_titles)

    concatenated_list = [
        f"{product} - {flavor} - {quantity}"
        for product, flavor, quantity in zip(product_title, flavor_title, quantity_title)
    ]

    try:

        prod_06 = exist_product_06.split(" - ")
        prod_05 = exist_product_05.split(" - ")
        prod_04 = exist_product_04.split(" - ")
        prod_03 = exist_product_03.split(" - ")
        prod_02 = exist_product_02.split(" - ")
        prod_01 = exist_product_01.split(" - ")

        expected_product_titles = [prod_06[0], prod_05[0], prod_04[0],
                                   prod_03[0], prod_02[0], prod_01[0]]

        expected_flavor_titles = [prod_06[1], prod_05[1], prod_04[1],
                                  prod_03[1], prod_02[1], prod_01[1]]

        expected_quantity_titles = [prod_06[2], prod_05[2], prod_04[2],
                                    prod_03[2], prod_02[2], prod_01[2]]

        product_title, flavor_title, quantity_title = context.cvp.verify_add_products(
            expected_product_titles, expected_flavor_titles,
            expected_quantity_titles)


        concatenated_list = [
            f"{product} - {flavor} - {quantity}"
            for product, flavor, quantity in zip(product_title, flavor_title, quantity_title)
        ]

        allure.attach(f"Expected Products{[exist_product_06, exist_product_05, exist_product_04, 
                                           exist_product_03, exist_product_02, exist_product_01]}",
                      name="Expected products added", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual products{concatenated_list}",
                      name="Actual products added", attachment_type=allure.attachment_type.TEXT)

    except Exception as e:
        allure.attach(f"Expected Products{[exist_product_06, exist_product_05, exist_product_04,
                                           exist_product_03, exist_product_02, exist_product_01]}",
                      name="Expected products added", attachment_type=allure.attachment_type.TEXT)
        allure.attach(f"Actual products{concatenated_list}",
                      name="Actual products added", attachment_type=allure.attachment_type.TEXT)

        raise Exception(f"Error in veryfing products: {e}")

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
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding Products. is successfully",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding Products. is unsuccessfully",
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
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking submit button: {e}")

@then(u'I Verify account name to submit order,')
def Verify_account_name(context):
    with allure.step(f"Yes is clicked"):
        try:
            context.cvp.Verify_account()
            allure.attach(context.driver.get_screenshot_as_png(), name="Verify account successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Verify account unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking submit button: {e}")

@then(u'I verify the Order Received landing page URL,')
def verify_order(context):
    with allure.step(f" Verify the landing page Url"):
        expected_url, actual_url = context.url.order_urls()
        print(expected_url)
        print(actual_url)
        try:
            time.sleep(10)
            context.url = UrlVerification(context.driver)
            print(expected_url)
            print(actual_url)
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
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking order placed: {e}")


@then(u'I Enter Order ID,')
def Order_ID(context):
    context.driver.implicitly_wait(20)
    (context.cvp.order_no("VALID_INPUTS", "ORDER_ID"))

@then(u'Order ID Verify,')
def Order_ID_Verify(context):
    context.driver.implicitly_wait(20)
    context.cvp.verify_order_received()


@when(u'I click Order Received Page,')
def Order_Received_Page(context):
    with allure.step(f"Order Received Page is clicked"):
        try:
            context.cvp.Order_Received_Page()
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order Placed unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking Order Received Page: {e}")


@then(u'I click search2 button,')

def search_2(context):
    with allure.step(f"search2 button is clicked"):
        try:
            context.cvp.search3()
            allure.attach(context.driver.get_screenshot_as_png(), name="Order_no searched successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Order_no searched unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"search2 button is clicked: {e}")

@then(u'I click view order,')

def view_order(context):
    with allure.step(f"view order is clicked"):
        try:
            context.cvp.view_order()
            allure.attach(context.driver.get_screenshot_as_png(), name="view order clicked successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="view order clicked unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"view order is not clicked: {e}")


@then(u'I click edit order,')
def edit_order(context):
    with allure.step(f"edit order is clicked"):
        try:
            context.cvp.generate_picking_slip()
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"edit order is not clicked: {e}")

@then(u'I compare the edit order data with pdf data,')
def edit_order_data(context):
    with allure.step(f"edit order data"):
        try:
            context.cvp.edit_order_data()
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order data generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order data generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"generate picking slip not clicked: {e}")





@then(u'I click generate picking slip,')
def generate_picking_slip(context):
    with allure.step(f"generate picking slip is clicked"):
        try:
            context.cvp.generate_picking_slip()
            allure.attach(context.driver.get_screenshot_as_png(), name="picking slip generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="picking slip generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"generate picking slip not clicked: {e}")



@then(u'I click edit order confirmation button,')

def confirmation(context):
    with allure.step(f"edit order confirmation button is clicked"):
        try:
            context.cvp.edit_order_confirmation_button()
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order confirmation button generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="edit order confirmation button generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"edit order confirmation button not clicked: {e}")

@when(u'I click download picking slip button,')
def download_picking_slip(context):
    with allure.step(f"download picking slip button is clicked"):
        try:
            context.cvp.download_picking_slip_button()
            allure.attach(context.driver.get_screenshot_as_png(), name="download picking slip button generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="download picking slip button generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"download picking slip button not clicked: {e}")


@when(u'I click on picking slip & shipment preparation page,')
def picking_slip_shipment_preparation_page(context):
    with allure.step(f" picking_slip_shipment_preparation_page is clicked"):
        try:
            context.cvp.picking_slip_and_shipment_page()
            allure.attach(context.driver.get_screenshot_as_png(), name="pickingslip_shipment_preparation_page Placed successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="pickingslip_shipment_preparation_page unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking picking_slip_shipment_preparation_page: {e}")



@then(u'I click edit order & validate picking slip,')
def edit_order_validate_picking_slip(context):
    with allure.step(f"download picking slip button is clicked"):
        try:
            context.cvp.edit_order_validate_picking_slip()
            allure.attach(context.driver.get_screenshot_as_png(), name="edit_order_validate_picking_slip button generated successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="edit_order_validate_picking_slip button generated unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"edit_order_validate_picking_slip button not clicked: {e}")

@then(u'I enter validation number,')
def validation(context):
    with allure.step(f"enter validation number"):
        try:
            context.cvp.validation()
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"validation number not successfully entered: {e}")

@then('I click order out for delivery,')
def order_out_for_delivery(context):
    with allure.step(f"I click order_out_for_delivery"):
        try:
            context.cvp.order_out_for_delivery()
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"order_out_for_delivery not clicked: {e}")


@then(u'I click Checkbox,')
def checkbox(context):
    with allure.step(f"I click checkbox"):
        try:
            context.cvp.checkbox()
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Checkbox not clicked: {e}")

@then(u'I click move to delivered,')
def move_to_delivered(context):
    with allure.step(f"I click move to delivered"):
        try:
            context.cvp.move_to_delivered()
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"move to delivered not clicked: {e}")



@then(u'I enter Confirmation,')
def Confirmation(context):
    with allure.step(f"Confirmation"):
        try:
            context.cvp.confirmation()
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Confirmation not successful: {e}")

def carrier_name(context):
    with allure.step(f"enter carrier name"):
        try:
            context.cvp.carrier_name()
            allure.attach(context.driver.get_screenshot_as_png(),
                          number="enter carrier name successfully",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),
                          number="enter carrier name unsuccessfully",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"validation number not successfully entered: {e}")

@then(u'I click proceed to shipment and document preparation,')
def shipment_and_document(context):

    with allure.step(f"shipment and document"):
        try:
            context.cvp.shipment_document()
            allure.attach(context.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),

                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"shipment and document not clicked: {e}")

    @then(u'I verify the choosed document type')
    def step_imp(context):
        with allure.step(f"Verify the choosed document type."):
            try:
                actual_doc_type = context.cvp.verify_document_type(doc_type_02)
                allure.attach(f"{doc_type_02}",
                              name="Expected document type", attachment_type=allure.attachment_type.TEXT)
                allure.attach(f"{actual_doc_type}",
                              name="Actual document type", attachment_type=allure.attachment_type.TEXT)


            except Exception as e:
                allure.attach(context.driver.get_screenshot_as_png(),
                              name="Document type selection is unsuccessfull",
                              attachment_type=allure.attachment_type.PNG)

                allure.attach(f"{doc_type_02}",
                              name="Expected document type", attachment_type=allure.attachment_type.TEXT)

                allure.attach(f"{actual_doc_type}",
                              name="Actual document type", attachment_type=allure.attachment_type.TEXT)
                raise Exception(f"Error in choosing document type: {e}")




