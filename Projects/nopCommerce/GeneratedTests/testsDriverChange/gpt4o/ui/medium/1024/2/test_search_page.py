import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check for navigation links
            nav_links = [
                (By.LINK_TEXT, "Home page"),
                (By.LINK_TEXT, "New products"),
                (By.LINK_TEXT, "Search"),
                (By.LINK_TEXT, "My account"),
                (By.LINK_TEXT, "Blog"),
                (By.LINK_TEXT, "Contact us")
            ]

            for by, value in nav_links:
                element = self.wait.until(EC.visibility_of_element_located((by, value)))
                self.assertTrue(element.is_displayed(), f"Element {value} is not visible")

            # Check for search input and button
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")

            # Check for form submit verification
            search_input.clear()
            search_input.send_keys("book")
            search_button.click()

            # Verify product listing
            product_items = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-item")))
            self.assertGreater(len(product_items), 0, "No products found")

            # Interaction check
            first_product = product_items[0]
            add_to_cart_button = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()

            # Check for potential visual updates (like cart quantity update, assuming success notification or such)
            cart_quantity = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-qty")))
            self.assertTrue(cart_quantity.is_displayed(), "Cart quantity is not visible")
            self.assertIn("1", cart_quantity.text, "Cart was not updated")

        except Exception as e:
            self.fail(f"Test failed due to error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()