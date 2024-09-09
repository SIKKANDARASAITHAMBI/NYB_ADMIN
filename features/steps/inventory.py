import time
from behave import *

from Dummy import test
from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.inventory import HeaderNavigators
from features.pages.login import Login
from features.pages.url_verification import UrlVerification
from features.pages.invoice_and_packing_slip import VendorPackingSlip
from features.utilities import ConfigReader


@given(u'I visit the NYB admin website and log in as a user with create, edit, and view access,')
def login(context):
    context.driver.implicitly_wait(20)
    context.driver.get(ConfigReader.urls("URL", "BASE_URL"))
    context.ln = Login(context.driver)
    context.ln.login_form(
        "SIGNIN VALID INPUT", "USER_NAME", "PASSWORD")


@then(u'I verify the orders module URL,')
def verify_create_order_url(context):
    context.driver.implicitly_wait(20)
    context.url = UrlVerification(context.driver)
    context.url.create_order_url()


@then(u'I navigate to the Inventory module,')
def inventory_nav(context):
    context.driver.implicitly_wait(20)
    context.hn = HeaderNavigators(context.driver)
    context.hn.inventory()


@then(u'I verify the inventory module URL,')
def verify_create_inbound_inventory_url(context):
    time.sleep(4)
    context.driver.implicitly_wait(20)
    context.url = UrlVerification(context.driver)
    context.url.create_inbound_inventory_url()


@then(u'I choose the document type as "vendor packing slip",')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp = CreateVendorPackingSlip(context.driver)
    context.cvp.document_type("VALID INPUTS", "SOURCE_TYPE01")


@then(u'I select the warehouse,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.warehouse("VALID INPUTS", "WAREHOUSE")


@then(u'I select the vendor,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.vendors("VALID INPUTS", "VENDORS")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO01),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO01")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO02),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO02")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO03),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO03")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO04),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO04")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO05),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO05")


@then(u'I enter a valid packing slip number(#Packing slip no -- NO06),')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO06")


@then(u'I upload the packing slip,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.upload_packing_slip()


@then(u'I add products,')
def step_impl(context):
    products = ["PRODUCT_NAME01", "PRODUCT_NAME02",
                "PRODUCT_NAME03", "PRODUCT_NAME04", "PRODUCT_NAME05", "PRODUCT_NAME06"]
    category = "VALID INPUTS"
    context.cvp.add_products(category, products)


@then(u'I click add sample product option,')
def step_impl(context):
    products = ["SAMPLE_OPTION"]
    category = "VALID INPUTS"

    context.cvp.add_products(category, products)


@then(u'I add new sample product,')
def step_impl(context):
    context.cvp.add_sample_products("VALID INPUTS", "NEW_SAMPLE_PRODUCT_OPTION")


@then(u'I click is sample product,')
def step_impl(context):
    context.cvp.is_sample_product()


@then(u'I enter a valid product name,')
def step_impl(context):
    context.cvp.sample_product_name("VALID INPUTS", "NEW_SAMPLE_PRODUCT_NAME")


@then(u'I enter a valid flavor name,')
def step_impl(context):
    context.cvp.sample_products_flavor_name("VALID INPUTS", "NEW_SAMPLE_PRODUCTS_FLAVOR_NAME")


@then(u'I enter a valid size/weight variant,')
def step_impl(context):
    context.cvp.sample_product_flavors_size_weight_variant_name("VALID INPUTS",
                                                                "NEW_SAMPLE_PRODUCTS_FLAVORS_SIZE_WEIGHT_VARIANT_NAME")
@then(u'I enter a valid price,')
def step_impl(context):
    pass


@then(u'I click confirm button,')
def step_impl(context):
    context.cvp.confirm()

@then(u'I enter a valid inward quantity, valid damaged quanity, valid unit price, valid batch number, valid expiry date,')
def inwardquantity_td01(context):
    context.driver.implicitly_wait(20)
    inward_quantities = ["INWARD_QTY01", "INWARD_QTY02","INWARD_QTY03",
                         "INWARD_QTY04", "INWARD_QTY05", "INWARD_QTY06" ]

    damaged_quantities = ["DAMAGED_QTY01", "DAMAGED_QTY02", "DAMAGED_QTY03",
                          "DAMAGED_QTY04", "DAMAGED_QTY05", "DAMAGED_QTY06"]

    unit_prices = ["UNIT_PRICE01", "UNIT_PRICE02", "UNIT_PRICE03",
                   "UNIT_PRICE04", "UNIT_PRICE05", "UNIT_PRICE06"]

    batch_nos = ["BATCH_NO01", "BATCH_NO02", "BATCH_NO03",
                 "BATCH_NO04", "BATCH_NO05", "BATCH_NO06"]

    expiry_dates = ["EXPIRY_DATE01", "EXPIRY_DATE02", "EXPIRY_DATE03",
                    "EXPIRY_DATE04", "EXPIRY_DATE05", "EXPIRY_DATE06"]

    context.cvp.vendor_packing_slip_table("VALID INPUTS", inward_quantities, damaged_quantities,
                                          unit_prices, batch_nos, expiry_dates)

@then(u'I click submit button.')
def submit(context):
    context.driver.implicitly_wait(20)
    context.cvp.submit()

@then(u'I verify the Invoice & Packing Slip landing page URL,')
def invocie_packing_slip_url(context):
    context.driver.implicitly_wait(20)
    context.url.invoice_and_packing_slip()

@then(u'I verify the autopopulated dates in the listing,')
def invoice_packing_slip_listing(context):
    context.vps = VendorPackingSlip(context.driver)
    context.vps.listing()


@then(u'I click the "View" button for the created entry,')
def invoice_packing_slip_view(context):
    context.driver.implicitly_wait(20)
    pass


@then(u'I verify that all the displayed details are correct.')
def invoice_packing_slip_view_details(context):
    context.driver.implicitly_wait(20)
    pass

# @then(u'I navigated to the invoice and packing slip page,')
# def inventory_nav(context):
#     context.driver.implicitly_wait(20)
#     context.hn.invoice_and_packingslip()





