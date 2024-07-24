from playwright.async_api import Page
from tests.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.accept_cookies_locator = page.locator('#ccc-recommended-settings')
        self.industry_link = page.locator('a.mega-menu__link.mega-menu__title:text("Industries")')
        self.search_button = page.locator('button[title="Search"]')
        self.search_input_field = page.locator('input[aria-label="Start your search..."]')
        self.search_button_submit = page.locator('button.btn.btn--icon-right.search__btn-submit.js-search__btn-submit')

    @property
    def expected_heading(self):
        return 'True partners change the world together'
    
    @property
    def expected_title(self):
        return 'Digital Transformation Experts and Workday Partners | Kainos'

    def navigate(self):
        self.page.goto(self.base_url, timeout=5000)

    def accept_cookies(self):
        self.accept_cookies_locator.click()

    def click_industry_link(self):
        self.industry_link.click()

    def search(self):
        self.search_button.click()
        self.search_input_field.fill('test')
        self.search_button_submit.click()



        