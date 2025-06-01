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
        self.driver.get('http://localhost:8080/en/')
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page (already opened in setUp)

        # Step 2: Click on a product category from the top navigation menu (e.g., ART).
        art_category_selector = (By.CSS_SELECTOR, 'a[href*="9-art"]')
        try:
            art_category = wait.until(EC.presence_of_element_located(art_category_selector))
            art_category.click()
        except Exception as e:
            self.fail(f"Art category link not found: {str(e)}")

        # Step 3: Wait for the category page to load by checking if products are visible.
        first_product_selector = (By.CSS_SELECTOR, '.js-product:nth-child(1) a.product-thumbnail')
        try:
            first_product = wait.until(EC.presence_of_element_located(first_product_selector))
            first_product.click()
        except Exception as e:
            self.fail(f"First product link not found: {str(e)}")

        # Step 4: Click on the first product in the list.
        add_to_cart_button_selector = (By.CSS_SELECTOR, 'button.add-to-cart')
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_button_selector))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to Cart button not found: {str(e)}")

        # Step 5: Wait for the modal popup to appear after adding to cart.
        modal_selector = (By.ID, 'blockcart-modal')
        modal_title_selector = (By.CSS_SELECTOR, '#blockcart-modal .modal-title')
        try:
            modal = wait.until(EC.visibility_of_element_located(modal_selector))
            modal_title = driver.find_element(*modal_title_selector).text
        except Exception as e:
            self.fail(f"Cart modal not appearing or no title: {str(e)}")

        # Step 6: Confirm that the modal title or content includes a success message.
        if "successfully added" not in modal_title.lower():
            self.fail("Success message not found in modal title")

        # Step 7: Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        proceed_to_checkout_button_selector = (By.CSS_SELECTOR, '#blockcart-modal a.btn-primary')
        try:
            proceed_to_checkout_button = driver.find_element(*proceed_to_checkout_button_selector)
            if not proceed_to_checkout_button.is_displayed():
                self.fail("Proceed to checkout button is not visible")
        except Exception as e:
            self.fail(f"Proceed to checkout button not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()