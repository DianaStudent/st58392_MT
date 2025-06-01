from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Verify header is visible
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header)

            # Verify footer is visible
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer)

            # Verify navigation menu
            nav_menu = wait.until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
            self.assertIsNotNone(nav_menu)

            # Verify search input is visible
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            self.assertIsNotNone(search_input)

            # Verify "Subscribe" button is visible
            subscribe_button = wait.until(EC.visibility_of_element_located((By.NAME, "submitNewsletter")))
            self.assertIsNotNone(subscribe_button)

            # Verify sections like sidebar filters and product list
            sidebar = wait.until(EC.visibility_of_element_located((By.ID, "left-column")))
            self.assertIsNotNone(sidebar)
            
            products_section = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertIsNotNone(products_section)

            # Verify "Sign in" link is visible
            sign_in_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))
            self.assertIsNotNone(sign_in_link)

            # Verify that "Art" text is present
            art_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Art']")))
            self.assertIsNotNone(art_text)

            # Click and verify that cart is visible
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            cart_button.click()

            cart_count = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-products-count")))
            self.assertIn("(0)", cart_count.text)

        except Exception as e:
            # If any essential element is missing, fail the test
            self.fail(f"UI element missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()