import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        
        # Define elements to check
        elements_to_check = [
            (By.XPATH, "//div[@class='logo']/a/img"),  # Logo
            (By.LINK_TEXT, "Home"),  # Home link
            (By.LINK_TEXT, "Tables"),  # Tables link
            (By.LINK_TEXT, "Chairs"),  # Chairs link
            (By.XPATH, "//button[@aria-label='Accept cookies']"),  # Accept cookies button
            (By.XPATH, "//button[@class='account-setting-active']"),  # Account setting button
            (By.XPATH, "//button[@class='icon-cart']"),  # Cart icon
            (By.XPATH, "//input[@type='email']"),  # Email subscription field
            (By.XPATH, "//button[text()='Subscribe']")  # Subscribe button
        ]
        
        # Check that each element is present and visible
        for locator in elements_to_check:
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
                self.assertTrue(element.is_displayed(), f"Element {locator} is not visible.")
            except Exception as e:
                self.fail(f"Failed to find and display the element: {locator} - Exception: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()