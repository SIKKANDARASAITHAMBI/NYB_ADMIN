import configparser
import os
import time

import allure
from behave import *

from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.inventory import HeaderNavigators
from features.pages.url_verification import UrlVerification
from features.utilities import ConfigReader

doc_type_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE01")
doc_type_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE02")
doc_type_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE03")
warehouse_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "WAREHOUSE")
vendor_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "VENDORS_01")
tax_no_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "TAX")
discount = ConfigReader.create_inbound_inventory("VALID INPUTS", "DISCOUNT")
invoice_no_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "VENDOR_INVOICE_NO")
upload_invoice1 = os.path.abspath("./documents/file-example_PDF_1MB.pdf")
upload_discount_proof = os.path.abspath("./documents/file-example_PDF_1MB.pdf")
exist_product_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME01")
exist_product_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME02")
exist_product_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME03")
exist_product_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME04")
exist_product_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME05")
exist_product_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "PRODUCT_NAME06")
new_pts_fls_samples = ConfigReader.create_inbound_inventory("VALID INPUTS", "SAMPLE_OPTION")

inward_quantities_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY01")
inward_quantities_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY02")
inward_quantities_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY03")
inward_quantities_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY04")
inward_quantities_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY05")
inward_quantities_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "INWARD_QTY06")

damaged_quantities_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY01")
damaged_quantities_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY02")
damaged_quantities_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY03")
damaged_quantities_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY04")
damaged_quantities_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY05")
damaged_quantities_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "DAMAGED_QTY06")

unit_prices_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE01")
unit_prices_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE02")
unit_prices_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE03")
unit_prices_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE04")
unit_prices_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE05")
unit_prices_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "UNIT_PRICE06")

batch_nos_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO01")
batch_nos_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO02")
batch_nos_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO03")
batch_nos_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO04")
batch_nos_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO05")
batch_nos_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "BATCH_NO06")

expiry_dates_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE01")
expiry_dates_02 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE02")
expiry_dates_03 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE03")
expiry_dates_04 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE04")
expiry_dates_05 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE05")
expiry_dates_06 = ConfigReader.create_inbound_inventory("VALID INPUTS", "EXPIRY_DATE06")

is_sample_01 = True
is_sample_02 = False

product_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                   "NEW_SAMPLE_PRODUCT_NAME01")
product_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                   "NEW_SAMPLE_PRODUCT_NAME02")
product_03 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                   "NEW_SAMPLE_PRODUCT_NAME03")
product_04 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                   "NEW_SAMPLE_PRODUCT_NAME04")

flavor_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                  "NEW_FLAVOR_NAME01")
flavor_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                  "NEW_FLAVOR_NAME02")
flavor_03 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                  "NEW_FLAVOR_NAME03")
flavor_04 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                  "NEW_FLAVOR_NAME04")

quantity_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                        "NEW_SIZE_WEIGHT01")
quantity_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                        "NEW_SIZE_WEIGHT02")
quantity_03 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                        "NEW_SIZE_WEIGHT03")
quantity_04 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                        "NEW_SIZE_WEIGHT04")

price_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                     "NEW_PRICE_01")
price_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                     "NEW_PRICE_02")
price_03 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                     "NEW_PRICE_03")
price_04 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                     "NEW_PRICE_04")


# **************************** Inventory Header Nav ****************************

@when(u'I navigate to the Inventory module and verified the landing page URL,')
def inventory_nav(context):
    with allure.step(f"Navigating to the inventory module > Create Inbound Inventory page"):
        try:
            context.hn = HeaderNavigators(context.driver)
            context.hn.header_navs("inventory")
            allure.attach(context.driver.get_screenshot_as_png(), name="Inventory page navigation successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Inventory page navigation unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error during login: {e}")

    with allure.step(f"Verify the landing page Url"):
        try:
            context.url = UrlVerification(context.driver)
            expected_url, actual_url = context.url.inventory_urls()
            allure.attach(f"{expected_url}",
                          name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_url}",
                          name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)
        except Exception as e:
            allure.attach(f"{expected_url}",
                          name="Expected Page URL", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_url}",
                          name="Actual Page URL", attachment_type=allure.attachment_type.TEXT)


# **************************** Common ****************************

@when(u'I select the warehouse,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.warehouse("VALID INPUTS", "WAREHOUSE")


@when(u'I select the vendor,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.vendors("VALID INPUTS", "VENDORS")


@when(u'I select the new vendor,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.vendors("VALID INPUTS", "VENDORS_01")


@when(u'I Enter vendor name,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.vendor_name("VALID INPUTS", "VENDOR_NAME")


@when(u'I add products,')
def add_products(context):
    with allure.step(f"""added products:
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

@then(u'I verify the added products')
def verify_added_products(context):

    concatenated_list = []

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


@when(u'I click add sample product option,')
def step_impl(context):
    product = [new_pts_fls_samples]
    context.cvp.add_products(product)


@then(u'I click is sample product,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.is_sample_product()
    context.driver.implicitly_wait(20)


@then(u'I enter a valid product name,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    products = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_SAMPLE_PRODUCT_NAME02", "NEW_SAMPLE_PRODUCT_NAME03",
                "NEW_SAMPLE_PRODUCT_NAME04", "NEW_SAMPLE_PRODUCT_NAME05", "NEW_SAMPLE_PRODUCT_NAME06"]
    category = "VALID INPUTS"
    context.cvp.add_sample_products(category, products)
    allure.attach(context.driver.get_screenshot_as_png(), name="New_Products",
                  attachment_type=allure.attachment_type.PNG)


@then(u'I enter a valid flavor name,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.sample_products_flavor_name("VALID INPUTS", "NEW_SAMPLE_PRODUCTS_FLAVOR_NAME")


@then(u'I enter a valid size/weight variant,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.sample_product_flavors_size_weight_variant_name("VALID INPUTS",
                                                                "NEW_SAMPLE_PRODUCTS_FLAVORS_SIZE_WEIGHT_VARIANT_NAME")


@then(u'I enter a valid price,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.sample_product_price("VALID INPUTS", "NEW_VALID_PRICE")


@when(u'I click confirm button,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.confirm()
    context.driver.implicitly_wait(20)
    allure.attach(context.driver.get_screenshot_as_png(), name="confirm", attachment_type=allure.attachment_type.PNG)


def test_datas():
    inward_quantities = ["INWARD_QTY01", "INWARD_QTY02", "INWARD_QTY03",
                         "INWARD_QTY04", "INWARD_QTY05", "INWARD_QTY06"]

    damaged_quantities = ["DAMAGED_QTY01", "DAMAGED_QTY02", "DAMAGED_QTY03",
                          "DAMAGED_QTY04", "DAMAGED_QTY05", "DAMAGED_QTY06"]

    unit_prices = ["UNIT_PRICE01", "UNIT_PRICE02", "UNIT_PRICE03",
                   "UNIT_PRICE04", "UNIT_PRICE05", "UNIT_PRICE06"]

    batch_nos = ["BATCH_NO01", "BATCH_NO02", "BATCH_NO03",
                 "BATCH_NO04", "BATCH_NO05", "BATCH_NO06"]

    expiry_dates = ["EXPIRY_DATE01", "EXPIRY_DATE02", "EXPIRY_DATE03",
                    "EXPIRY_DATE04", "EXPIRY_DATE05", "EXPIRY_DATE06"]

    return inward_quantities, damaged_quantities, unit_prices, batch_nos, expiry_dates


def test_datas2():
    new_product_name = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_SAMPLE_PRODUCT_NAME02", "NEW_SAMPLE_PRODUCT_NAME03",
                        "NEW_SAMPLE_PRODUCT_NAME04", "NEW_SAMPLE_PRODUCT_NAME05", "NEW_SAMPLE_PRODUCT_NAME06"]

    new_flavor_name = ["NEW_FLAVOR_NAME01", "NEW_FLAVOR_NAME02", "NEW_FLAVOR_NAME03",
                       "NEW_FLAVOR_NAME04", "NEW_FLAVOR_NAME05", "NEW_FLAVOR_NAME06"]

    new_size_weight = ["NEW_SIZE_WEIGHT01", "NEW_SIZE_WEIGHT02", "NEW_SIZE_WEIGHT03",
                       "NEW_SIZE_WEIGHT04", "NEW_SIZE_WEIGHT05", "NEW_SIZE_WEIGHT06"]

    new_price = ["NEW_PRICE_01", "NEW_PRICE_02", "NEW_PRICE_03"
                                                 "NEW_PRICE_04", "NEW_PRICE_05", "NEW_PRICE_06"]

    return new_product_name, new_flavor_name, new_size_weight, new_price


@when(
    u'I enter a valid inward quantity, valid damaged quantity, valid unit price, valid batch number, valid expiry date,')
def inward_quantity(context):
    with (allure.step(f"""added inward quantity:
                              quantity1: {inward_quantities_01},
                              quantity2: {inward_quantities_02},
                              quantity3: {inward_quantities_03},
                              quantity4: {inward_quantities_04},
                              quantity5: {inward_quantities_05},
                              quantity6: {inward_quantities_06},
                              
                      added damaged quantity:
                          damaged quantity1: {damaged_quantities_01},
                          damaged quantity2: {damaged_quantities_02},
                          damaged quantity3: {damaged_quantities_03},
                          damaged quantity4: {damaged_quantities_04},
                          damaged quantity5: {damaged_quantities_05},
                          damaged quantity6: {damaged_quantities_06},
                          
                      added unit price:
                          unit price01: {unit_prices_01},
                          unit price02: {unit_prices_02},
                          unit price03: {unit_prices_03},
                          unit price04: {unit_prices_04},
                          unit price05: {unit_prices_05},
                          unit price06: {unit_prices_06},
                          
                      added batch_nos:
                          batch_nos01: {batch_nos_01},
                          batch_nos02: {batch_nos_02},
                          batch_nos03: {batch_nos_03},
                          batch_nos04: {batch_nos_04},
                          batch_nos05: {batch_nos_05},
                          batch_nos06: {batch_nos_06},
                          
                      added expiry_dates:
                          expiry_dates01: {expiry_dates_01},
                          expiry_dates02: {expiry_dates_02},
                          expiry_dates03: {expiry_dates_03},
                          expiry_dates04: {expiry_dates_04},
                          expiry_dates05: {expiry_dates_05},
                          expiry_dates06: {expiry_dates_06},"""
                      )):
        try:
            inward_qty = [inward_quantities_01, inward_quantities_02, inward_quantities_03, inward_quantities_04,
                          inward_quantities_05, inward_quantities_06]

            damaged_qty = [damaged_quantities_01, damaged_quantities_02, damaged_quantities_03,
                           damaged_quantities_04, damaged_quantities_05, damaged_quantities_06]
            unit_prices = [unit_prices_01, unit_prices_02, unit_prices_03, unit_prices_04, unit_prices_05,
                           unit_prices_06]
            batch_numbers = [batch_nos_01, batch_nos_02, batch_nos_03, batch_nos_04, batch_nos_05, batch_nos_06]
            expiry_dates = [expiry_dates_01, expiry_dates_02, expiry_dates_03, expiry_dates_04, expiry_dates_05,
                            expiry_dates_06]

            context.cvp.table(inward_qty, damaged_qty, unit_prices, batch_numbers, expiry_dates)
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding datas to the product is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Adding data to the product is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"""Error Adding Products:""" f"{e}")

    '''
    context.driver.implicitly_wait(20)
    inward_quantities, damaged_quantities, unit_prices, batch_nos, expiry_dates = test_datas()
    context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
                      unit_prices, batch_nos, expiry_dates)
    allure.attach(context.driver.get_screenshot_as_png(), name="pdt_details",
                 attachment_type=allure.attachment_type.PNG)
    '''


'''
@then(u'I enter a valid product name, flavor name, size weight, and price,')
def Product(context):
    context.driver.implicitly_wait(20)
    new_product_name, new_flavor_name, new_size_weight, new_price = test_datas2()
    context.cvp.table2("VALID INPUTS", new_product_name, new_flavor_name, new_size_weight, new_price)
    allure.attach(context.driver.get_screenshot_as_png(), name="pdt_details", attachment_type=allure.attachment_type.PNG)
'''


@when(u'I enter Purchase Order No,')
def purchase_order_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.purchase_order_no("VALID INPUTS", "PURCHASE_ORDER_NO")


@when(u'I click submit button.')
def submit(context):
    with allure.step(f"Submit button clicked"):
        try:
            context.cvp.submit()
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Submit unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error in clicking submit button: {e}")


@then(u'I verify the choosed document type, warehouse , and vendor,')
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

    with allure.step(f"Verify the choosed warehouse."):
        try:
            actual_warehouse = context.cvp.verify_warehouse(warehouse_01)
            allure.attach(f"{warehouse_01}",
                          name="Expected warehouse", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_warehouse}",
                          name="Actual warehouse", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Warehouse selection is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)

            allure.attach(f"{warehouse_01}",
                          name="Expected warehouse", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_warehouse}",
                          name="Actual warehouse", attachment_type=allure.attachment_type.TEXT)
            raise Exception(f"Error in choosing warehouse: {e}")

    with allure.step(f"Verify the choosed vendor."):
        try:
            actual_vendor = context.cvp.verify_vendor(vendor_01)
            allure.attach(f"{vendor_01}",
                          name="Expected vendor", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_vendor}",
                          name="Actual vendor", attachment_type=allure.attachment_type.TEXT)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(),
                          name="Vendor selection is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            allure.attach(f"{vendor_01}",
                          name="Expected vendor", attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"{actual_vendor}",
                          name="Actual vendor", attachment_type=allure.attachment_type.TEXT)
            raise Exception(f"Error in choosing vendor: {e}")


# **************************** Vendor Packing Slip ****************************

@then(u'I verify the orders module URL,')
def verify_create_order_url(context):
    context.driver.implicitly_wait(20)
    context.url = UrlVerification(context.driver)
    context.url.order_urls("create order")


@when(u'I choose the document type as "vendor packing slip",')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.document_type("VALID INPUTS", "SOURCE_TYPE01")


@when(u'I Enter packing slip number,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.pk_no("VALID INPUTS", "PKNO01")


@when(u'I Enter packing slip number1,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.pk_no("VALID INPUTS", "PKNO02")


@when(u'I upload the packing slip,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.upload_packing_slip("C:/Users/hp/Desktop/nyb.PNG")


# **************************** Vendor Invoice ***************************

@when(u'I choose the document type as "Vendor Invoice", select warehouse, and select vendor')
def vendor_invoice_source(context):
    with allure.step(f"{doc_type_02} selected as document type"):
        try:
            context.cvp.document_type(doc_type_02)
            allure.attach(context.driver.get_screenshot_as_png(), name="Document type selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Document type selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting document type '{doc_type_02}': {e}")

    with allure.step(f"{warehouse_01} selected as warehouse"):
        try:
            context.cvp.warehouse(warehouse_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Warehouse selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Warehouse selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting warehouse '{warehouse_01}': {e}")

    with allure.step(f"{vendor_01} selected as vendor"):
        try:
            context.cvp.vendors(vendor_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Vendor selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Vendor selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting vendor '{vendor_01}': {e}")

    with allure.step(f"added inward quantity:\n"
                     f"quantity1: {inward_quantities_01},\n"
                     f"quantity2: {inward_quantities_02},\n"
                     f"quantity3: {inward_quantities_03},\n"
                     f"quantity4: {inward_quantities_04},\n"
                     f"quantity5: {inward_quantities_05},\n"
                     f"quantity6: {inward_quantities_06},\n"
                     f"added damaged quantity:\n"
                     f"damaged quantity1: {inward_quantities_01}\n,"
                     f"damaged quantity2: {inward_quantities_02}\n,"
                     f"damaged quantity3: {inward_quantities_03}\n,"
                     f"damaged quantity4: {inward_quantities_04}\n,"
                     f"damaged quantity5: {inward_quantities_05}\n,"
                     f"damaged quantity6: {inward_quantities_06}\n,"
                     ):
        pass


@when(u'I Enter Vendor Invoice No,')
def vendor_invoice_no(context):
    with allure.step(f"Invoice No: {invoice_no_01} entered"):
        try:
            context.driver.implicitly_wait(20)
            context.cvp.vendor_invoice_no(invoice_no_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering vendor invoice no. is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering vendor invoice no. is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error entering vendor no: '{invoice_no_01}': {e}")


@when(u'I Upload the Invoice,')
def upload_invoice(context):
    with allure.step(f"Uploading Invoice: {upload_invoice1} "):
        try:
            context.driver.implicitly_wait(20)
            context.cvp.upload_invoicee(upload_invoice1)
            allure.attach(context.driver.get_screenshot_as_png(), name="Invoice Upload. is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Invoice Upload. is not successfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error entering vendor no: {upload_invoice1}: {e}")


@when(u'I enter discount amount,')
def discounts(context):
    with allure.step(f"discount {discount} entered "):
        try:
            context.driver.implicitly_wait(20)
            context.cvp.discounts(discount)
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering discount. is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering discount. is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error entering discount : '{discount}': {e}")


@when(u'I enter tax amount,')
def tax(context):
    with allure.step(f"tax No {tax_no_01} entered "):
        try:
            context.driver.implicitly_wait(20)
            context.cvp.tax(tax_no_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering tax no. is successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Entering tax no. is unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error entering tax no: '{tax_no_01}': {e}")


@when(u'I enter other charges,')
def other_charges(context):
    context.driver.implicitly_wait(20)
    context.cvp.other_charges("VALID INPUTS", "OTHER_CHARGES")


# @then(
#     u'I enter a valid Intrawarehouse inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,')
# def inwardquantity_td01(context):
#     context.driver.implicitly_wait(20)
#     inward_quantities = ["INWARD_QTY01", "INWARD_QTY02", "INWARD_QTY03",
#                          "INWARD_QTY04", "INWARD_QTY05", "INWARD_QTY06"]
#
#     damaged_quantities = ["DAMAGED_QTY01", "DAMAGED_QTY02", "DAMAGED_QTY03",
#                           "DAMAGED_QTY04", "DAMAGED_QTY05", "DAMAGED_QTY06"]
#
#     unit_prices = ["UNIT_PRICE01", "UNIT_PRICE02", "UNIT_PRICE03",
#                    "UNIT_PRICE04", "UNIT_PRICE05", "UNIT_PRICE06"]
#
#     batch_nos = ["BATCH_NO01", "BATCH_NO02", "BATCH_NO03",
#                  "BATCH_NO04", "BATCH_NO05", "BATCH_NO06"]
#
#     expiry_dates = ["EXPIRY_DATE01", "EXPIRY_DATE02", "EXPIRY_DATE03",
#                     "EXPIRY_DATE04", "EXPIRY_DATE05", "EXPIRY_DATE06"]
#
#     doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE03")
#     context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
#                       unit_prices, batch_nos, expiry_dates, doc_type)


# @then(
#     u'I enter a valid Payment Receipt inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,')
# def inwardquantity_td01(context):
#     context.driver.implicitly_wait(20)
#     inward_quantities = ["INWARD_QTY01", "INWARD_QTY02", "INWARD_QTY03",
#                          "INWARD_QTY04", "INWARD_QTY05", "INWARD_QTY06"]
#
#     damaged_quantities = ["DAMAGED_QTY01", "DAMAGED_QTY02", "DAMAGED_QTY03",
#                           "DAMAGED_QTY04", "DAMAGED_QTY05", "DAMAGED_QTY06"]
#
#     unit_prices = ["UNIT_PRICE01", "UNIT_PRICE02", "UNIT_PRICE03",
#                    "UNIT_PRICE04", "UNIT_PRICE05", "UNIT_PRICE06"]
#
#     batch_nos = ["BATCH_NO01", "BATCH_NO02", "BATCH_NO03",
#                  "BATCH_NO04", "BATCH_NO05", "BATCH_NO06"]
#
#     expiry_dates = ["EXPIRY_DATE01", "EXPIRY_DATE02", "EXPIRY_DATE03",
#                     "EXPIRY_DATE04", "EXPIRY_DATE05", "EXPIRY_DATE06"]
#
#     doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE05")
#     context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
#                       unit_prices, batch_nos, expiry_dates, doc_type)


# **************************** Intrawarehouse transfer ****************************

@when(u'I choose the document type as "IntrawarehouseTransfer Invoice",')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.document_type("VALID INPUTS", "SOURCE_TYPE03")
    allure.attach(context.driver.get_screenshot_as_png(), name="Doc_type", attachment_type=allure.attachment_type.PNG)


@when(u'I select the from warehouse,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.from_warehouse("VALID INPUTS", "WAREHOUSE_FROM")
    allure.attach(context.driver.get_screenshot_as_png(), name="From_warehouse",
                  attachment_type=allure.attachment_type.PNG)


@when(u'I select the to warehouse,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.to_warehouse("VALID INPUTS", "WAREHOUSE_TO")
    allure.attach(context.driver.get_screenshot_as_png(), name="To_warehouse",
                  attachment_type=allure.attachment_type.PNG)


@when(u'I enter the number,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.intra_ware_house_transfer_no("VALID INPUTS", "NO")
    allure.attach(context.driver.get_screenshot_as_png(), name="Number", attachment_type=allure.attachment_type.PNG)


@when(u'Upload the Transfer Invoice,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.upload_transfer_invoices("C:/Users/sikku/Downloads"
                                         "/Woodbolt_Distribution_cellucor_Packing_slip_11_27_2024.pdf")
    allure.attach(context.driver.get_screenshot_as_png(), name="Doc_upload", attachment_type=allure.attachment_type.PNG)


# **************************** Payment Receipts ****************************


@when(u'I choose the document type as "Payment_Reciept",')
def Payment_Reciepts(context):
    context.cvp.document_type("VALID INPUTS", "SOURCE_TYPE05")


@when(u'I enter Payment Receipt No,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO")


@when(u'I enter Payment Receipt No1,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_01")


@when(u'I enter Payment Receipt No2,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_02")


@when(u'I enter Payment Receipt No3,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_03")


@when(u'I enter Payment Receipt No4,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_04")


@when(u'I enter Payment Receipt No5,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_05")


@when(u'I enter Payment Receipt No6,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_06")


@when(u'I enter Payment Receipt No7,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_07")


@when(u'I enter Payment Receipt No8,')
def payment_receipt_number(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_receipt_no("VALID INPUTS", "PAYMENT_RECEIPT_NO_08")


@when(u'I upload the receipt,')
def step_impl(context):
    context.cvp.upload_invoicee("C:/Users/hp/Desktop/nyb.PNG")


@when(u'I upload Document Proof For Discount,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.document_proof_ids('C:/Users/hp/Desktop/nyb.PNG')


@when('I add Document Proof For Discount,')
def add_doc_proof(context):
    context.cvp.document_proof_for_discount(upload_discount_proof)


@when(u'I enter notes,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.notes("VALID INPUTS", "NOTES")


@when(u'I Select the Payment Mode,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_mode("VALID INPUTS", "PAYMENT_MODE_CHECK")


@then(u'I enter a valid product name, flavor name, size weight, and price,')
def add_new_product(context):
    context.driver.implicitly_wait(20)

    new_product_name = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_SAMPLE_PRODUCT_NAME02"]

    new_flavor_name = ["NEW_FLAVOR_NAME01", "NEW_FLAVOR_NAME02"]

    new_size_weight = ["NEW_SIZE_WEIGHT01", "NEW_SIZE_WEIGHT02"]

    new_price = ["NEW_PRICE_01", "NEW_PRICE_02"]

    # doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE02")
    context.cvp.table2("VALID INPUTS", new_product_name, new_flavor_name, new_size_weight, new_price)


@when(u'I add new sample products,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    product_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                       "NEW_PRODUCT_01")
    product_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                       "NEW_PRODUCT_02")
    product_03 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                       "NEW_PRODUCT_03")

    products = [product_03, product_03, product_03]
    context.cvp.add_sample_products(products)


@when('I enter add new product, add new flavor, add new size weight(New combination),')
def add_new_product_product(context):
    is_sample_products = [is_sample_01, is_sample_02, is_sample_01,
                          is_sample_02]

    new_products = [product_01, product_02, product_03, product_04]

    new_flavors = [flavor_01, flavor_02, flavor_03, flavor_04]

    new_quantity = [quantity_01, quantity_02, quantity_03, quantity_04]

    prices = [price_01, price_02, price_03, price_04]

    context.cvp.sample_product_table(is_sample_products, new_products, new_flavors,
                                     new_quantity, prices)

@when(u'I add new sample products in existing combination,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    product_01 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                       "NEW_PRODUCT_01")
    product_02 = ConfigReader.create_inbound_inventory("VALID INPUTS",
                                                       "NEW_PRODUCT_02")

    products = [product_01, product_02]
    context.cvp.add_sample_products(products)


@when('I enter add new product, add new flavor, add new size weight(existing combination),')
def add_new_product_product(context):
    is_sample_01 = True
    is_sample_02 = False
    is_sample_products = [is_sample_01, is_sample_02, is_sample_01,
                          is_sample_02, is_sample_01, is_sample_02]

    context.cvp.sample_product_table_existing_combo(is_sample_products)


@then('I enter productname,')
def enter_product_name(context):
    context.driver.implicitly_wait(20)
    context.cvp.enter_items("VALID INPUTS", "ENTER_PRODUCT_NAME")
    context.driver.implicitly_wait(20)

@then('I choose the document type as "Vendor Packing Slip", select warehouse, and select vendor,')

def vendor_invoice_source(context):
    with allure.step(f"{doc_type_01} selected as document type"):
        try:
            context.cvp.document_type(doc_type_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Document type selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Document type selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting document type '{doc_type_01}': {e}")

    with allure.step(f"{warehouse_01} selected as warehouse"):
        try:
            context.cvp.warehouse(warehouse_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Warehouse selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Warehouse selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting warehouse '{warehouse_01}': {e}")

    with allure.step(f"{vendor_01} selected as vendor"):
        try:
            context.cvp.vendors(vendor_01)
            allure.attach(context.driver.get_screenshot_as_png(), name="Vendor selection successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Vendor selection unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error selecting vendor '{vendor_01}': {e}")
