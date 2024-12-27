import allure
from behave import *

from features.Inventory.pages.url_verification import UrlVerification
from features.Inventory.utilities import ConfigReader

doc_type_01 = ConfigReader.create_inbound_inventory("VALID INPUTS", "SOURCE_TYPE01")
filter_value = ConfigReader.vendor_invoices_and_packing_slips(
    "VALID INPUTS", "FILTER_04")


#**************************** VI&PS URL verification ***************************

@then(u'I verify the Invoice & Packing Slip landing page URL,')
def invoice_packing_slip_url(context):
    with allure.step(f" Verify the landing page Url"):
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
    with allure.step(f"Use {filter_value} filter"):
        try:
            context.page.filters(filter_value)
            allure.attach(context.driver.get_screenshot_as_png(), name="Filter successfull",
                          attachment_type=allure.attachment_type.PNG)

        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="Filter unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error filtering '{filter_value}': {e}")


#**************************** Listing ***************************

@then(u'I verify that the document is successfully created and displayed,')
def entry(context):
    try:
        context.vi.listing()
        allure.attach(context.driver.get_screenshot_as_png(), name="Listing verified successfully",
                      attachment_type=allure.attachment_type.PNG)

    except Exception as e:
        allure.attach(context.driver.get_screenshot_as_png(), name="Listing verified unsuccessfully",
                      attachment_type=allure.attachment_type.PNG)
        raise Exception(f"{e}")


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


