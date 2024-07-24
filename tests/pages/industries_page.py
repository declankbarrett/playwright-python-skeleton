from playwright.async_api import Page
from tests.pages.base_page import BasePage

class IndustriesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    @property
    def expected_heading(self):
        return 'Industry knowledge and digital expertise combined'
    
    @property
    def expected_title(self):
        return 'Industries'
