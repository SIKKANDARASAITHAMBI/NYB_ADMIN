import configparser
import time

import allure
from behave import *

from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.inbound_inventory_report import inbound_inventory_report
from features.pages.inventory import HeaderNavigators
from features.pages.invoice_and_packing_slip import VendorPackingSlip, Page
from features.pages.login import Login
from features.pages.url_verification import UrlVerification
from features.utilities import ConfigReader


# **************************** Inventory Header Nav ****************************

@when(u'I navigate to the Inventory module,')
def inventory_nav(context):
    context.driver.implicitly_wait(20)
    context.hn = HeaderNavigators(context.driver)
    context.hn.header_navs("inventory")
    allure.attach(context.driver.get_screenshot_as_png(), name="Inventory_module", attachment_type=allure.attachment_type.PNG)


# **************************** CIBI URL verification ****************************

@then(u'I verify the inventory module URL,')
def verify_create_inbound_inventory_url(context):
    time.sleep(1)
    context.driver.implicitly_wait(20)
    context.url = UrlVerification(context.driver)
    context.url.inventory_urls()


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
def step_impl(context):
    context.driver.implicitly_wait(20)
    products = ["PRODUCT_NAME01", "PRODUCT_NAME02",
                "PRODUCT_NAME03", "PRODUCT_NAME04", "PRODUCT_NAME05", "PRODUCT_NAME06"]
    category = "VALID INPUTS"
    context.cvp.add_products(category, products)
    allure.attach(context.driver.get_screenshot_as_png(), name="Products", attachment_type=allure.attachment_type.PNG)


@when(u'I click add sample product option,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    products = "SAMPLE_OPTION"
    category = "VALID INPUTS"

    context.cvp.add_products(category, products)


@then(u'I add new sample product,')
def step_impl(context):

    context.driver.implicitly_wait(20)
    context.cvp.add_sample_products()
    context.driver.implicitly_wait(20)




@then(u'I click is sample product,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.is_sample_product()
    context.driver.implicitly_wait(20)


@then(u'I enter a valid product name,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    products = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_SAMPLE_PRODUCT_NAME02","NEW_SAMPLE_PRODUCT_NAME03",
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


@then(u'I click confirm button,')
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


@when(u'I enter a valid inward quantity, valid damaged quantity, valid unit price,'
      u' valid batch number, valid expiry date,')
def inward_quantity(context):
    context.driver.implicitly_wait(20)
    inward_quantities, damaged_quantities, unit_prices, batch_nos, expiry_dates = test_datas()
    context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
                      unit_prices, batch_nos, expiry_dates)
    allure.attach(context.driver.get_screenshot_as_png(), name="pdt_details", attachment_type=allure.attachment_type.PNG)
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
    context.driver.implicitly_wait(20)
    context.cvp.submit()
    context.driver.implicitly_wait(20)
    allure.attach(context.driver.get_screenshot_as_png(), name="submit", attachment_type=allure.attachment_type.PNG)


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
    context.cvp.upload_packing_slip("C:/Users/sikku/Downloads"
                                    "/Woodbolt_Distribution_cellucor_Packing_slip_11_27_2024.pdf")


# **************************** Vendor Invoice ***************************

@when(u'I choose the document type as "Vendor Invoice",')
def vendor_invoice_source(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.document_type("VALID INPUTS", "SOURCE_TYPE02")


@when(u'I Enter Vendor Invoice No,')
def vendor_invoice_no(context):
    context.driver.implicitly_wait(20)
    context.cvp.vendor_invoice_no("VALID INPUTS", "VENDOR_INVOICE_NO")


@when(u'I Upload the Invoice,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.upload_invoicee("C:/Users/hp/Desktop/nyb.PNG")


@when(u'I enter discount amount,')
def discounts(context):
    context.driver.implicitly_wait(20)
    context.cvp.discounts("VALID INPUTS", "DISCOUNT")


@when(u'I enter tax amount,')
def tax(context):
    context.driver.implicitly_wait(20)
    context.cvp.tax("VALID INPUTS", "TAX")


@when(u'I enter other charges,')
def other_charges(context):
    context.driver.implicitly_wait(20)
    context.cvp.other_charges("VALID INPUTS", "OTHER_CHARGES")


@then(
    u'I enter a valid Intrawarehouse inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,')
def inwardquantity_td01(context):
    context.driver.implicitly_wait(20)
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

    doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE03")
    context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
                      unit_prices, batch_nos, expiry_dates, doc_type)


@then(
    u'I enter a valid Payment Receipt inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,')
def inwardquantity_td01(context):
    context.driver.implicitly_wait(20)
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

    doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE05")
    context.cvp.table("VALID INPUTS", inward_quantities, damaged_quantities,
                      unit_prices, batch_nos, expiry_dates, doc_type)


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
    allure.attach(context.driver.get_screenshot_as_png(), name="From_warehouse", attachment_type=allure.attachment_type.PNG)

@when(u'I select the to warehouse,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.to_warehouse("VALID INPUTS", "WAREHOUSE_TO")
    allure.attach(context.driver.get_screenshot_as_png(), name="To_warehouse", attachment_type=allure.attachment_type.PNG)


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
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
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
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.upload_invoicee(
        "C:/Users/sikku/Downloads"
        "/Woodbolt_Distribution_cellucor_Packing_slip_11_27_2024.pdf")


@when(u'I upload Document Proof For Discount,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.document_proof_ids("C:/Users/sikku/Downloads"
                                   "/Woodbolt_Distribution_cellucor_Packing_slip_11_27_2024.pdf")


@when(u'I enter notes,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.notes("VALID INPUTS", "NOTES")


@when(u'I Select the Payment Mode,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.payment_mode("VALID INPUTS", "PAYMENT_MODE_CHECK")

'''
@when(u'I click add sample product option,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    products = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_PRODUCT_NAME02",
                "NEW_PRODUCT_NAME03", "NEW_PRODUCT_NAME04", "NEW_PRODUCT_NAME05", "NEW_PRODUCT_NAME06"]
    category = "VALID INPUTS"
    context.cvp.add_sample_products(category, products)
    allure.attach(context.driver.get_screenshot_as_png(), name="New_Products", attachment_type=allure.attachment_type.PNG)
'''
@then(u'I enter a valid product name, flavor name, size weight, and price,')
def add_new_product(context):
    context.driver.implicitly_wait(20)

    new_product_name = ["NEW_SAMPLE_PRODUCT_NAME01", "NEW_SAMPLE_PRODUCT_NAME02"]

    new_flavor_name = ["NEW_FLAVOR_NAME01", "NEW_FLAVOR_NAME02"]

    new_size_weight = ["NEW_SIZE_WEIGHT01", "NEW_SIZE_WEIGHT02"]

    new_price = ["NEW_PRICE_01", "NEW_PRICE_02"]



    #doc_type = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE02")
    # context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.table2("VALID INPUTS", new_product_name,  new_flavor_name, new_size_weight, new_price)