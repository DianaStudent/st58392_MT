import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 1: Open the home page (already done in setUp)

        # Step 2: Click on a product category from the top navigation menu (e.g., ART)
        try:
            art_category = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]'))
            )
            art_category.click()
        except:
            self.fail("Art category not found or unable to click.")

        # Step 3: Wait for the category page to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#js-product-list'))
            )
        except:
            self.fail("Category page failed to load.")

        # Step 4: Click on the first product in the list
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href^="http://localhost:8080/en/art/"]'))
            )
            first_product.click()
        except:
            self.fail("First product not found or unable to click.")

        # Step 5: On the product detail page, click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'button.add-to-cart'))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or unable to click.")

        # Step 6: Wait for the modal popup to appear after the product is added
        try:
            modal_popup = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div#blockcart-modal'))
            )
        except:
            self.fail("Modal popup did not appear.")

        # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.modal-title'))
            )
            self.assertIn("successfully added", success_message.text.lower())
        except:
            self.fail("Success message not found or does not contain 'successfully added'.")

        # Step 8: Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        try:
            proceed_to_checkout = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'a.btn.btn-primary[href*="/en/cart?action=show"]'))
            )
            self.assertTrue(proceed_to_checkout.is_displayed())
        except:
            self.fail("Proceed to checkout button not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()