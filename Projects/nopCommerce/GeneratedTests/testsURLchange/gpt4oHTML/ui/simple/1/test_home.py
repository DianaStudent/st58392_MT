import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check headers presence
        self._check_element_presence((By.CLASS_NAME, "header"))
        self._check_element_presence((By.CLASS_NAME, "header-upper"))
        self._check_element_presence((By.CLASS_NAME, "header-lower"))
        
        # Check links presence and visibility
        self._check_element_presence((By.LINK_TEXT, "Register"))
        self._check_element_presence((By.LINK_TEXT, "Log in"))
        
        # Check form fields
        self._check_element_presence((By.ID, "small-search-box-form"))
        self._check_element_presence((By.ID, "small-searchterms"))
        
        # Check buttons
        self._check_element_presence((By.CLASS_NAME, "button-1"))
        
        # Check footer
        self._check_element_presence((By.CLASS_NAME, "footer"))
        
        # Validate element visibility
        self._is_element_visible((By.CLASS_NAME, "header-links-wrapper"))
        self._is_element_visible((By.CLASS_NAME, "header-menu"))
        self._is_element_visible((By.ID, "newsletters-email"))
        
    def _check_element_presence(self, locator):
        """Check that a UI element is present in the DOM"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
        except (TimeoutException, NoSuchElementException):
            self.fail(f"Element {locator} was not found in the page.")

    def _is_element_visible(self, locator):
        """Check that a UI element is visible"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.fail(f"Element {locator} is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()