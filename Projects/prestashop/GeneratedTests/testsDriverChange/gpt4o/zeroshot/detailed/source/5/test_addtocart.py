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

        # Step 1: Click on the ART category in the top menu
        art_category = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='9-art']"))
        )
        art_category.click()

        # Step 2: Wait for the category page to load and click on the first product
        first_product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product-miniature a.product-thumbnail"))
        )
        first_product.click()

        # Step 3: On the product detail page, click the "Add to cart" button
        add_to_cart_btn = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_btn.click()

        # Step 4: Wait for the modal popup to appear
        modal = self.wait.until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )

        # Step 5: Confirm the modal title or content includes a success message
        modal_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-title"))
        )

        if not modal_title or "successfully added" not in modal_title.text:
            self.fail("Success message not found in modal title")
        
        # Step 6: Locate and assert the presence of a "Proceed to checkout" button
        proceed_to_checkout_btn = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-content-btn .btn-primary"))
        )

        if not proceed_to_checkout_btn:
            self.fail("Proceed to checkout button not found in modal")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()