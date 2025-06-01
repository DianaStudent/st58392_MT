import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Step 2: Click on a product category from the top navigation menu (e.g., ART)
            art_category = wait.until(
                EC.presence_of_element_located((By.LINK_TEXT, "Art"))
            )
            art_category.click()

            # Step 3: Wait for the category page to load
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "category-id-9"))
            )

            # Step 4: Click on the first product in the list
            first_product = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".js-product a.thumbnail.product-thumbnail")
                )
            )
            first_product.click()

            # Step 5: On the product detail page, click the "Add to cart" button
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, ".add-to-cart")
                )
            )
            add_to_cart_button.click()

            # Step 6: Wait for the modal popup to appear after the product is added
            modal = wait.until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )

            # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
            modal_title = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "#blockcart-modal .modal-title")
                )
            )
            self.assertIn("successfully added", modal_title.text.lower())

            # Step 8: Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
            checkout_button = wait.until(
                EC.presence_of_element_located(
                    (By.LINK_TEXT, "Proceed to checkout")
                )
            )
            self.assertTrue(checkout_button.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()