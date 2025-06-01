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

    def test_add_to_cart_process(self):
        driver = self.driver

        # Navigate to the Art category
        category_art = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/en/9-art']"))
        )
        category_art.click()

        # Open product detail page for "The best is yet to come' Framed poster"
        product_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
        )
        product_link.click()

        # Add the product to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the add-to-cart modal to appear
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-title"))
        )

        # Confirm the success of adding to cart
        if "successfully added" not in modal_title.text.lower():
            self.fail("Product was not added successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()