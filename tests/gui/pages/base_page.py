from abc import ABC, abstractmethod
from utils.accessibility_check import run_accessibility

class BasePage(ABC):
    
    base_url = 'https://www.kainos.com'

    def __init__(self, page):
        self.page = page
        self.heading = page.locator('h1')
        

    @property
    @abstractmethod
    def expected_heading(self):
        pass

    @property
    @abstractmethod
    def expected_title(self):
        pass


    def get_heading(self):
        return self.heading.inner_text()
    
    def check_heading(self):
        actual_heading = self.get_heading()
        assert actual_heading == self.expected_heading, (
            f"Expected heading to be '{self.expected_heading}' but got '{actual_heading}'"
        )
    
    def check_title(self):
        actual_title = self.page.title()
        assert actual_title == self.expected_title, (
            f"Expected title to be '{self.expected_title}' but got '{actual_title}'"
        )

    def check_accessibility(self):
        run_accessibility(self.page)
    
