import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on a product category (e.g. from the top menu).
        try:
            clothes_category = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '3-clothes')]"))
            )
            clothes_category.click()
        except Exception as e:
            self.fail(f"Could not click on Clothes category: {e}")

        # 3. Select the first product listed in the category.
        try:
            first_product = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//article[contains(@class, 'product-miniature')]//a[contains(@class, 'product-thumbnail')]"))
            )
            first_product.click()
        except Exception as e:
            self.fail(f"Could not click on the first product: {e}")

        # 4. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on Add to cart button: {e}")

        # 5. Wait for the modal popup that confirms the product was added to the cart.
        try:
            modal = wait.until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {e}")

        # 6. Verify the modal contains a message like "Product successfully added to your shopping cart".
        try:
            modal_title_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
            )
            modal_title_text = modal_title_element.text
            self.assertIn("Product successfully added to your shopping cart", modal_title_text)
        except Exception as e:
            self.fail(f"Could not verify modal title: {e}")

if __name__ == "__main__":
    unittest.main()