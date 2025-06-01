from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertIsNotNone(header)
        except:
            self.fail("Header not visible")

        # Check footer elements
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertIsNotNone(footer)
        except:
            self.fail("Footer not visible")

        # Check search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located(
                (By.ID, "small-searchterms")))
            self.assertIsNotNone(search_input)
        except:
            self.fail("Search input not visible")

        # Check search button
        try:
            search_button = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "search-box-button")))
            self.assertIsNotNone(search_button)
            search_button.click()
        except:
            self.fail("Search button not visible or clickable")
        
        # Check product filters and product items
        try:
            product_filters = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "product-filters")))
            self.assertIsNotNone(product_filters)
            
            products_container = wait.until(EC.visibility_of_element_located(
                (By.CLASS_NAME, "products-container")))
            self.assertIsNotNone(products_container)
        except:
            self.fail("Product filters or container not visible")

        # Interact with the "Add to cart" button of the first product
        try:
            add_to_cart_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
            self.assertIsNotNone(add_to_cart_button)
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not visible or clickable")

        # Confirm UI reacts visually (e.g., flyout cart showing is activated)
        try:
            flyout_cart = wait.until(EC.visibility_of_element_located(
                (By.ID, "flyout-cart")))
            self.assertTrue(flyout_cart.is_displayed())
        except:
            self.fail("Flyout cart not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()