from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_key_elements_present(self):
        # Wait for key elements to be present
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//nav[@role='navigation']"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
            )

        except TimeoutException:
            self.fail("Key UI elements not present")

    def test_navigation_button_clickable(self):
        # Wait for navigation button to be clickable
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='navigation-button']"))
            )
            nav_button = self.driver.find_element(By.XPATH, "//button[@id='navigation-button']")
            nav_button.click()

        except TimeoutException:
            self.fail("Navigation button not clickable")

    def test_search_input_present(self):
        # Wait for search input to be present
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
            )

        except TimeoutException:
            self.fail("Search input not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()