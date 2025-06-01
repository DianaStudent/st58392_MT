import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Step 1: Click on a product category
            category = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            category.click()

            # Step 2: Select the first product listed in the category
            first_product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '3-13-the-best-is-yet-to-come-framed-poster.html')]"))
            )
            first_product.click()

            # Step 3: Add product to the cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart')]"))
            )
            add_to_cart_button.click()

            # Step 4: Wait for the modal to confirm the product was added
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h4[contains(@id, 'myModalLabel') and contains(text(), 'successfully added')]"))
            )

            # Step 5: Verify the modal message
            self.assertTrue(modal_title.is_displayed(), "Modal title not displayed")
            self.assertIn("successfully added", modal_title.text, "Add to cart confirmation not found in modal text.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()