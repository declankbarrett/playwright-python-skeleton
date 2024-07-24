from playwright.async_api import Page
from tests.pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.accept_cookies_locator = page.locator('#ccc-recommended-settings')

    @property
    def expected_heading(self):
        return 'True partners change the world together'

    def navigate(self):
        self.page.goto(self.base_url, timeout=5000)

    def accept_cookies(self):
        self.accept_cookies_locator.click()