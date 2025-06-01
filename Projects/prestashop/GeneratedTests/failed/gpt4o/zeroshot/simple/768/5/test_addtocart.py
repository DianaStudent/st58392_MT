from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Navigate to Art category
            art_category = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category.click()
            
            # Click on the product 'The best is yet to come' Framed poster
            product_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), \"The best is yet to come' Framed poster\")]"))
            )
            product_link.click()

            # Click 'Add to cart' button
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
            )
            add_to_cart_button.click()

            # Wait for the confirmation modal and verify success message
            modal_title = wait.until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]")
                )
            )
            self.assertIsNotNone(modal_title, "Modal title for success not found.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()