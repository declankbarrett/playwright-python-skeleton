import time
from behave import given, when, then
from pages.home_page import HomePage


@given('I navigate to the Kainos homepage')
def step_given_i_am_on_homepage(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate()

@when('I accept cookies')
def accept_cookies(context):
    context.home_page.accept_cookies()
    time.sleep(3)


@then('I should have a valid title')
def check_title(context):
    context.home_page.check_heading()