import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to the "Art" category
        art_category_link = self.wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Art"))
        )
        art_category_link.click()

        # Click on the product "The best is yet to come' Framed poster"
        product_link = self.wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "The best is yet to come"))
        )
        product_link.click()

        # Add product to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the confirmation modal to appear
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal.in .modal-title"))
        )

        # Verify the success message in the modal
        if "Product successfully added" not in modal_title.text:
            self.fail("Success message not found in modal after adding product to cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()