import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SimpleUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check the header is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "header"))), "Header not visible")

        # Check the footer is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "footer"))), "Footer not visible")

        # Check the main content section is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "main"))), "Main section not visible")

        # Check the search widget is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget"))), "Search widget not visible")

        # Check the product list is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list"))), "Product list not visible")

        # Check 'Contact us' link is present and visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))), "'Contact us' link not visible")

        # Check 'Sign in' button is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))), "'Sign in' button not visible")

        # Check 'Cart' button is visible
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart"))), "'Cart' button not visible")

        # Interact with a button and confirm UI reaction
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shopping-cart")))
        cart_button.click()

        # Assert that no required UI element is missing
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
        except Exception as e:
            self.fail(f"Required UI element not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()