import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Click on the 'Art' category from the top navigation menu
        art_category = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#category-9 a'))
        )
        art_category.click()

        # Wait for the Art category page to load and click on the first product
        first_product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#js-product-list .product-miniature a'))
        )
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.add-to-cart'))
        )
        add_to_cart_button.click()

        # Wait for the modal popup to appear after the product is added
        modal_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#blockcart-modal .modal-title'))
        )

        # Confirm the modal content includes the success message "successfully added"
        self.assertIn("successfully added", modal_title.text.lower())

        # Assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#blockcart-modal a.btn-primary'))
        )

        if not proceed_to_checkout_button.is_displayed():
            self.fail("Proceed to checkout button not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()