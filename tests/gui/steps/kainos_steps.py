# In this file I am using time.sleep to slow the tests down, this is not neccessary, it is just for visual clarification the steps are performing as expected when run in headed mode
import time
from behave import given, when, then
from pages.home_page import HomePage
from tests.gui.pages.industries_page import IndustriesPage
from tests.gui.pages.search_page import SearchPage

@given('I navigate to the Kainos homepage')
def step_given_i_am_on_homepage(context):
    context.home_page = HomePage(context.page)
    context.home_page.navigate()

@when('I accept cookies')
def accept_cookies(context):
    context.home_page.accept_cookies()
    time.sleep(1)


@then('I should have a valid title for homepage')
def check_title(context):
    context.home_page.check_heading()
    context.home_page.check_title()
    time.sleep(1)

# The 'And' steps in behave are replaced by the preceding step, so for example the previous step before this in the feature file was "Then I should have a valid title for homepage", 
# therefore the "And" step after it takes a "Then" prefix
@then('I click on the industries link')
def click_industry(context):
    context.home_page.click_industry_link()
    time.sleep(1)

@then('I should have a valid title for industries page')
def check_title(context):
    context.industries_page = IndustriesPage(context.page)
    context.industries_page.check_heading()
    context.industries_page.check_title()
    time.sleep(1)

@then('I search for test in the search bar')
def search_step(context):
    context.home_page.search()
    time.sleep(1)

@then('I should have a valid title for search results page')
def check_search_results(context):
    context.search_page = SearchPage(context.page)
    context.search_page.check_search_content()
    time.sleep(1)

@then('I check accessibility for the homepage')
def check_homepage_accessibility(context):
    context.home_page.check_accessibility()

@then('I check accessibility for the industries page')
def check_homepage_accessibility(context):
    context.industries_page.check_accessibility()