from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Navigate to the home page
        self.driver.get("http://localhost/")

        # Check main UI components are present and visible on home page
        self._check_element_present_and_visible(By.TAG_NAME, "h1")
        self._check_element_present_and_visible(By.ID, "home-button")

        # Navigate to tables page
        self.driver.get("http://localhost/category/tables")

        # Check main UI components are present and visible on tables page
        self._check_element_present_and_visible(By.TAG_NAME, "h2")
        self._check_element_present_and_visible(By.LINK_TEXT, "Chairs")
        self._check_element_present_and_visible(By.NAME, "search")

        # Navigate to chairs page
        self.driver.get("http://localhost/category/chairs")

        # Check main UI components are present and visible on chairs page
        self._check_element_present_and_visible(By.TAG_NAME, "h3")
        self._check_element_present_and_visible(By.LINK_TEXT, "Login")
        self._check_element_present_and_visible(By.NAME, "filter")

        # Navigate to login page
        self.driver.get("http://localhost/login")

        # Check main UI components are present and visible on login page
        self._check_element_present_and_visible(By.TAG_NAME, "h4")
        self._check_element_present_and_visible(By.NAME, "username")
        self._check_element_present_and_visible(By.NAME, "password")

        # Navigate to register page
        self.driver.get("http://localhost/register")

        # Check main UI components are present and visible on register page
        self._check_element_present_and_visible(By.TAG_NAME, "h5")
        self._check_element_present_and_visible(By.NAME, "name")
        self._check_element_present_and_visible(By.NAME, "email")

    def _check_element_present_and_visible(self, locator_type, locator_value):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((locator_type, locator_value)))
        except:
            self.fail(f"Element '{locator_value}' is missing from the page.")

if __name__ == "__main__":
    unittest.main()