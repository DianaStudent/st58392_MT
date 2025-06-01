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

        # Step 2: Click on the ART category from the top navigation menu
        art_category_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/en/9-art')]"))
        )
        art_category_link.click()

        # Step 3: Wait for the category page to load
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.page-category"))
        )

        # Step 4: Click on the first product in the list
        first_product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product a.product-thumbnail"))
        )
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn-primary.add-to-cart"))
        )
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        modal_popup = self.wait.until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # Step 7: Confirm that the modal title or content includes a success message
        modal_title = modal_popup.find_element(By.ID, "myModalLabel")
        self.assertIn("successfully added", modal_title.text.lower())

        # Step 8: Assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = modal_popup.find_element(By.XPATH, "//a[contains(@href, 'cart?action=show')]")
        self.assertIsNotNone(proceed_to_checkout_button)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()