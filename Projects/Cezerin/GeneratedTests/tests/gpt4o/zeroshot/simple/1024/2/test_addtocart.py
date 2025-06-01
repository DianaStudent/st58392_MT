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
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Navigate to Category A
            category_a = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Category A"))
            )
            category_a.click()

            # Navigate to Product A
            product_a = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Product A"))
            )
            product_a.click()

            # Add to Cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart .button"))
            )
            add_to_cart_button.click()

            # Click on Cart Button
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button img"))
            )
            cart_button.click()

            # Ensure "GO TO CHECKOUT" Button is Present
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "GO TO CHECKOUT"))
            )

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()