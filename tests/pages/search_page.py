from playwright.async_api import Page
from tests.pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.test_search_result = page.locator('text="Kainos Smart: Smart Test for Workday"')

    
    @property
    def expected_heading(self):
        pass
    
    @property
    def expected_title(self):
        return 'Search'
    
    def check_search_content(self):
        is_visible = self.test_search_result.is_visible()
        assert is_visible, "The Smart Test link is not visible on the page."
