from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Header
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))

            # Footer
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))

            # Navigation
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))

            # Search Input
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))

            # Language Selector
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "_desktop_language_selector")))

            # Sign In Link
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))

            # Cart
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "_desktop_cart")))

            # Categories
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))

            # Contact Us Link
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/contact-us']")))

            # Products
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "products")))

            # Perform click on first product
            first_product = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-miniature a.thumbnail")))
            first_product.click()

            # Wait for quick view to be visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "quick-view")))

        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction failure: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()