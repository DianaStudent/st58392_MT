from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Click on ART category
            art_category = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category.click()

            # Wait for category page to load and click on first product
            first_product = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@class='thumbnail product-thumbnail']"))
            )
            first_product.click()

            # Wait for product detail page to load and click "Add to cart"
            add_to_cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary.add-to-cart"))
            )
            add_to_cart_button.click()

            # Wait for the modal to appear, then confirm success message
            modal = self.wait.until(
                EC.presence_of_element_located((By.ID, "blockcart-modal"))
            )

            modal_title = modal.find_element(By.CLASS_NAME, "modal-title")
            self.assertIn("successfully added", modal_title.text)

            # Verify presence of "Proceed to checkout" button
            proceed_to_checkout_button = modal.find_element(By.XPATH, "//a[contains(@href, '/en/cart?action=show')]")
            self.assertTrue(proceed_to_checkout_button)

        except TimeoutException:
            self.fail("An expected element was not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()