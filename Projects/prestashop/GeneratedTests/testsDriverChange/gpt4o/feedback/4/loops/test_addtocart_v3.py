from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on ART category
        art_category = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/9-art"]')
        ))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.products')
        ))

        # Step 4: Click on the first product in the list
        first_product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.products a.product-thumbnail')
        ))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button.add-to-cart')
        ))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        modal = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'div.modal#blockcart-modal')
        ))

        # Step 7: Confirm that the modal title or content includes a success message
        modal_title = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'h4.modal-title')
        ))
        self.assertIn("successfully added", modal_title.text, "Success message not found in modal title")

        # Step 8: Locate and assert the presence of "Proceed to checkout" button
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a.btn-primary')
        ))
        self.assertIsNotNone(proceed_to_checkout_button, "Proceed to checkout button is missing in the modal")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()