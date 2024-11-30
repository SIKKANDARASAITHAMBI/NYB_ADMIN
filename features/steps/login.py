from behave import *

from features.pages.login import Login
from features.utilities import ConfigReader


#**************************** Login ****************************

@given(u'I visit the NYB admin website and log in as a user with create, edit, and view access,')
def login(context):
    context.driver.implicitly_wait(20)
    context.driver.get(ConfigReader.urls("URL", "BASE_URL"))
    context.ln = Login(context.driver)
    context.ln.login_form(
        "SIGNIN VALID INPUT", "USER_NAME", "PASSWORD")
