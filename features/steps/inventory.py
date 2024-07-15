import time

from behave import *

from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.inventory import HeaderNavigators
from features.pages.login import Login
from features.pages.url_verification import UrlVerification
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
    context.cvp.add_products("VALID INPUTS", "PRODUCT_NAME")


@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY01),')
def inwardquantity_td01(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY01")

@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY02),')
def inwardquantity_td02(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY02")

@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY03),')
def inwardquantity_td03(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY03")

@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY04),')
def inwardquantity_td04(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY04")

@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY05),')
def inwardquantity_td05(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY05")

@then(u'I enter a valid inward quantity (#Inward Quantity -- INWARD_QTY06),')
def inwardquantity_td06(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY06")


@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY01),')
def damagedquantity_td01(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY01")

@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY02),')
def damagedquantity_td02(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY02")

@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY03),')
def damagedquantity_td03(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY03")

@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY04),')
def damagedquantity_td04(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY04")

@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY05),')
def damagedquantity_td05(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY05")

@then(u'I enter a valid damaged quantity (#Damaged Quantity -- DAMAGED_QTY06),')
def damagedquantity_td06(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY06")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE01),')
def unitprice_td01(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE01")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE02),')
def unitprice_td02(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE02")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE03),')
def unitprice_td03(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE03")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE04),')
def unitprice_td04(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE04")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE05),')
def unitprice_td05(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE05")

@then(u'I enter the unit price (#Unit Price -- UNIT_PRICE06),')
def unitprice_td06(context):
    context.driver.implicitly_wait(20)
    context.cvp.unit_price("VALID INPUTS", "UNIT_PRICE06")


@then(u'I enter the batch number,')
def batch_no(context):
    context.driver.implicitly_wait(20)
    context.cvp.batch_number("VALID INPUTS", "BATCH_NO")


@then(u'I enter the expiry date,')
def expiry_date(context):
    context.driver.implicitly_wait(20)
    context.cvp.expiry_date("VALID INPUTS", "EXPIRY_DATE")

@then(u'I click submit button.')
def submit(context):
    context.driver.implicitly_wait(20)
    context.cvp.submit()