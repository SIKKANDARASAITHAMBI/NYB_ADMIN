from behave import *

from features.pages.create_inbound_inventory import CreateVendorPackingSlip
from features.pages.inventory import HeaderNavigators
from features.pages.login import Login
from features.pages.url_verification import UrlVerification
from features.utilities import ConfigReader


@given(u'I visit the Chote Kisan website and log in as a user with create, edit, and view access,')
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


@then(u'I enter a valid packing slip number,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.no("VALID INPUTS", "NO")


@then(u'I upload the packing slip,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.upload_packing_slip()


@then(u'I add products,')
def step_impl(context):
    context.cvp.add_products("VALID INPUTS", "PRODUCT_NAME")


@then(u'I enter a valid inward quantity,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.inward_quantity("VALID INPUTS", "INWARD_QTY01")


@then(u'I enter a valid damaged quantity,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.damaged_quantity("VALID INPUTS", "DAMAGED_QTY05")


@then(u'I enter the unit price,')
def step_impl(context):
    context.driver.implicitly_wait(20)


@then(u'I enter the batch number,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.batch_number("VALID INPUTS", "BATCH_NO")


@then(u'I enter the expiry date.')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.cvp.expiry_date("VALID INPUTS", "EXPIRY_DATE")
