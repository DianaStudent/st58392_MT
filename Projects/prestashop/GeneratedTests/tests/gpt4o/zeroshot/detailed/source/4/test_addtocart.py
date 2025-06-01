import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "ART" category
        try:
            art_category_link = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#category-9 a[href*="9-art"]')
            ))
            art_category_link.click()
        except Exception:
            self.fail("ART category link not found or not clickable.")

        # Wait for the category page to load and click on the first product
        try:
            first_product_link = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.product-miniature a.product-thumbnail')
            ))
            first_product_link.click()
        except Exception:
            self.fail("First product link not found or not clickable.")

        # Click on "Add to cart" button on the product detail page
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, 'button.add-to-cart')
            ))
            add_to_cart_button.click()
        except Exception:
            self.fail("'Add to cart' button not found or not clickable.")

        # Wait for the modal to appear and check for success message
        try:
            modal_title = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, '#blockcart-modal .modal-title')
            ))
            self.assertIn("successfully added", modal_title.text.lower())
        except Exception:
            self.fail("Success message modal did not appear.")

        # Check for "Proceed to checkout" button
        try:
            proceed_to_checkout_button = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.cart-content-btn a[href*="cart?action=show"]')
            ))
            self.assertTrue(proceed_to_checkout_button.is_displayed())
        except Exception:
            self.fail("'Proceed to checkout' button not found or not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()