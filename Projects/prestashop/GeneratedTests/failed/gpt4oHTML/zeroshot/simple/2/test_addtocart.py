from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        
        # Navigate to home page and verify
        driver.get("http://localhost:8080/en/")
        
        # Locate and click on 'Art' category
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Art']"))
            )
            art_category_link.click()
        except:
            self.fail("Failed to find 'Art' category link")
        
        # Locate and click on 'The best is yet to come' Framed poster
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/art/3-13-the-best-is-yet-to-come-framed-poster.html')]"))
            )
            product_link.click()
        except:
            self.fail("Failed to find product link for 'The best is yet to come' Framed poster")

        # Add product to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Failed to click 'Add to cart'")
        
        # Wait for and verify the confirmation modal
        try:
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h4[contains(text(), 'successfully added')]"))
            )
            self.assertIn("successfully added", modal_title.text)
        except:
            self.fail("Confirmation modal with 'successfully added' message did not appear")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()