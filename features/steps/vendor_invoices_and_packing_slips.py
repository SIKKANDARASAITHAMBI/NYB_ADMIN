from behave import *

from features.pages.invoice_and_packing_slip import Page, VendorInvoice
from features.utilities import ConfigReader

#**************************** VI&PS URL verification ***************************

@then(u'I verify the Invoice & Packing Slip landing page URL,')
def invoice_packing_slip_url(context):
    context.driver.implicitly_wait(20)
    context.url.inventory_urls()

#**************************** Filters ***************************

@when(
    u'I filter the document no,')
def doc_no_filter(context):
    context.driver.implicitly_wait(20)
    context.page = Page(context.driver)
    filter_value = ConfigReader.vendor_invoices_and_packing_slips(
        "VALID INPUTS", "FILTER_04")
    context.page.filters(filter_value)

#**************************** Listing ***************************

@then(u'I verify that the document is successfully created and displayed,')
def entry(context):
    context.driver.implicitly_wait(20)
    context.vi = VendorInvoice(context.driver)
    step_name = "created document"
    context.vi.listing(step_name)


@then(u'I navigated to the vendor invoice and packing slip page,')
def inventory_nav(context):
    context.driver.implicitly_wait(20)
    context.hn.invoice_and_packingslip()


@then(u'I click view button,')
def view(context):
    context.driver.implicitly_wait(20)
    context.vps.view_update_vp_slip()
    context.driver.implicitly_wait(20)


@then(u'I Verify the navigated url is "Vendor Invoices and Packing Slips",')
def verify(context):
    context.driver.implicitly_wait(20)
    context.cvp.verify()
    context.driver.implicitly_wait(20)

