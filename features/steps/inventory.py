from behave import *

from features.pages.inventory import HeaderNavigators
from features.pages.login import Login
from features.pages.url_verification import UrlVerification
from features.utilities import ConfigReader


@given(u'I visit the Chote Kisan website and log in as a user with create, edit, and view access,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.driver.get(ConfigReader.urls("URL", "BASE_URL"))
    context.ln = Login(context.driver)
    context.ln.login_form()


@then(u'I verify the orders module URL,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.url = UrlVerification(context.driver)
    context.url.create_order_url()


@then(u'I navigate to the Inventory module,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.hn = HeaderNavigators(context.driver)
    context.hn.inventory()


@then(u'I verify the inventory module URL,')
def step_impl(context):
    context.driver.implicitly_wait(20)
    context.url.create_inbound_inventory_url()


@then(u'I choose the document type as "vendor packing slip",')
def step_impl(context):
    pass


@then(u'I select the warehouse,')
def step_impl(context):
    pass


@then(u'I select the vendor,')
def step_impl(context):
    pass


@then(u'I enter a valid packing slip number,')
def step_impl(context):
    pass


@then(u'I upload the packing slip,')
def step_impl(context):
    pass


@then(u'I add products,')
def step_impl(context):
    pass


@then(u'I enter a valid inward quantity,')
def step_impl(context):
    pass


@then(u'I enter a valid damaged quantity,')
def step_impl(context):
    pass


@then(u'I enter the unit price,')
def step_impl(context):
    pass


@then(u'I enter the batch number,')
def step_impl(context):
    pass


@then(u'I enter the expiry date.')
def step_impl(context):
    pass
