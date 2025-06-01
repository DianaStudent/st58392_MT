from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10) # implicit wait for the presence of elements
    
    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        # 1. Open the home page.
        # Already handled by driver.get()
        
        # 2. Click on a product category from the top navigation menu (e.g. ART).
        try:
            art_category = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.dropdown-item[href*="9-art"]'))
            )
            art_category.click()
        except TimeoutException:
            self.fail("Art category link not found on the home page.")
        
        # 3. Wait for the category page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.h1'))
            )
        except TimeoutException:
            self.fail("Category page did not load in time.")
        
        # 4. Click on the first product in the list.
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.thumbnail.product-thumbnail'))
            )
            first_product.click()
        except TimeoutException:
            self.fail("First product link not found on the category page.")
        
        # 5. On the product detail page, click the "Add to cart" button.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-primary.add-to-cart'))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Add to cart button not found on the product detail page.")
        
        # 6. Wait for the modal popup to appear after adding to cart.
        try:
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.modal-title'))
            )
        except TimeoutException:
            self.fail("Modal popup did not appear after adding product to cart.")
        
        # 7. Confirm that the modal title or content includes a success message like "successfully added".
        self.assertIn("successfully added", modal_title.text.lower(), 
                      "Success message not found in modal title.")
        
        # 8. Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal.
        try:
            proceed_to_checkout_button = driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
            self.assertTrue(proceed_to_checkout_button.is_displayed(), 
                            "Proceed to checkout button not found in the modal.")
        except NoSuchElementException:
            self.fail("Proceed to checkout button not found in the modal.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()