import allure
from behave import *

from features.pages.login import Login
from features.utilities import ConfigReader

# **************************** Login ****************************

admin_url = ConfigReader.urls("URL", "BASE_URL")
username = ConfigReader.login("SIGNIN VALID INPUT", "USER_NAME")
password = ConfigReader.login("SIGNIN VALID INPUT", "PASSWORD")


@given(u'I visit the NYB admin website and log in as a user with create, edit, and view access,')
def login(context):
    with allure.step(f"Navigating to the admin site: {admin_url}"):
        context.driver.get(admin_url)

    with allure.step(f"Login with {username} as username and {password} as password"):
        try:
            context.ln = Login(context.driver)
            context.ln.login_form(username, password)
            allure.attach(context.driver.get_screenshot_as_png(), name="login successfull",
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            allure.attach(context.driver.get_screenshot_as_png(), name="login unsuccessfull",
                          attachment_type=allure.attachment_type.PNG)
            raise Exception(f"Error during login: {e}")
