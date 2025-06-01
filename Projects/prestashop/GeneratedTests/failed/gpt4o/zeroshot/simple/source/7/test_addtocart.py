from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 1 - Access Art Category
        art_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Art'))
        )
        if not art_link:
            self.fail("Art category link not found.")
        art_link.click()

        # Step 2 - Click on a product
        product_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "The best is yet to come'..."))
        )
        if not product_link:
            self.fail("Product link not found.")
        product_link.click()

        # Step 3 - Add to cart
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn-primary.add-to-cart'))
        )
        if not add_to_cart_button:
            self.fail("Add to Cart button not found.")
        add_to_cart_button.click()

        # Step 4 - Confirm success by verifying modal
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-title.h6.text-sm-center'))
        )
        if not modal_title or "successfully added" not in modal_title.text.lower():
            self.fail("Product not successfully added to cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()