from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on ART category
        try:
            art_category = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')
            ))
        except Exception:
            self.fail("ART category link not found")
        art_category.click()

        # Step 3: Wait for the category page to load
        try:
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.products')
            ))
        except Exception:
            self.fail("Category page did not load")

        # Step 4: Click on the first product in the list
        try:
            first_product = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.products a.product-thumbnail')
            ))
        except Exception:
            self.fail("First product not found")
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'button.add-to-cart')
            ))
        except Exception:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        try:
            modal = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'div.modal#blockcart-modal')
            ))
        except Exception:
            self.fail("Add to cart confirmation modal did not appear")
        
        # Step 7: Confirm that the modal title includes a success message
        try:
            modal_title = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'h4.modal-title')
            ))
        except Exception:
            self.fail("Modal title not found")
        self.assertIn("successfully added", modal_title.text.lower(), "Success message not found in modal title")

        # Step 8: Locate and assert the presence of "Proceed to checkout" button
        try:
            proceed_to_checkout_button = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'a.btn-primary')
            ))
        except Exception:
            self.fail("Proceed to checkout button is missing in the modal")

        self.assertIsNotNone(proceed_to_checkout_button, "Proceed to checkout button is missing in the modal")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()