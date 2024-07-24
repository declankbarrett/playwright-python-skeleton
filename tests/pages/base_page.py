from abc import ABC, abstractmethod
from playwright.async_api import Page

class BasePage(ABC):
    
    base_url = 'https://www.kainos.com'

    def __init__(self, page):
        self.page = page
        self.heading = page.locator('h1')
        

    @property
    @abstractmethod
    def expected_heading(self):
        pass


    def get_heading(self):
        return self.heading.inner_text()
    
    def check_heading(self):
        actual_heading = self.get_heading()
        assert actual_heading == self.expected_heading, (
            f"Expected heading to be '{self.expected_heading}' but got '{actual_heading}'"
        )
    
