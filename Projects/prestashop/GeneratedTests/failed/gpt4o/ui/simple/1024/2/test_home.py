from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestHomepageUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header
            wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Verify navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Verify sign in link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Verify search bar
            wait.until(EC.visibility_of_element_located((By.NAME, "s")))

            # Verify cart
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))

            # Verify popular products section
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))

            # Verify newsletter subscription form
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))

            # Verify footer
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-footer")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()