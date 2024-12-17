import allure
from behave import *

from features.pages.inventory import HeaderNavigators
from features.pages.invoice_and_packing_slip import Page, VendorInvoice
from features.pages.url_verification import UrlVerification
from features.utilities import ConfigReader

#**************************** VI&PS URL verification ***************************

@then(u'I verify the Invoice & Packing Slip landing page URL,')
def invoice_packing_slip_url(context):
    #context.driver.implicitly_wait(20)
   # context.url.inventory_urls()
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


#**************************** Filters ***************************

@when(
    u'I filter the document no,')
def doc_no_filter(context):
    context.driver.implicitly_wait(20)
    context.page = Page(context.driver)
    filter_value = ConfigReader.vendor_invoices_and_packing_slips(
        "VALID INPUTS", "FILTER_04")
    context.page.filters(filter_value)
    allure.attach(context.driver.get_screenshot_as_png(), name="Filter", attachment_type=allure.attachment_type.PNG)

#**************************** Listing ***************************

@then(u'I verify that the document is successfully created and displayed,')
def entry(context):



    context.driver.implicitly_wait(20)
    context.vi = VendorInvoice(context.driver)
    step_name = "created document"
    context.vi.listing(step_name)
    allure.attach(context.driver.get_screenshot_as_png(), name="Listing", attachment_type=allure.attachment_type.PNG)



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

