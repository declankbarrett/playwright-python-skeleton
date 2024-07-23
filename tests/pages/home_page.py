from playwright.async_api import Page

class HomePage:
    def __init__(self, page):
        self.page = page
        self.title = page.locator('h1')
        self.accept_cookies_locator = page.locator('#ccc-recommended-settings')


    def navigate(self):
        self.page.goto("https://www.kainos.com", timeout=5000)

    def getHeading(self):
        return self.title.inner_text()

    def accept_cookies(self):
        self.accept_cookies_locator.click()