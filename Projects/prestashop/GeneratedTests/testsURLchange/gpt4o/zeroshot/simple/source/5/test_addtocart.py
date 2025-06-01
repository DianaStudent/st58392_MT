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

        # Navigate to "Art" category
        art_category = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
        )
        art_category.click()

        # Click on product "The best is yet to come' Framed poster"
        product = self.wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "The best is yet to come'..."))
        )
        product.click()

        # Add product to cart
        add_to_cart_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the modal to confirm product addition
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h4.modal-title"))
        )

        # Verify modal title contains success message
        self.assertIn("successfully added", modal_title.text.lower())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()