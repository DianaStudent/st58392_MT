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
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Step 1: Navigate to the "Art" category
            art_category_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
            art_category_link.click()
            
            # Step 2: Select "The best is yet to come' Framed poster" product
            product_link = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[href*='the-best-is-yet-to-come-framed-poster.html']")
            ))
            product_link.click()
            
            # Step 3: Add the product to the cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
            add_to_cart_button.click()

            # Step 4: Wait for modal to appear and verify success
            modal_title = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//h4[contains(text(), 'successfully added to your shopping cart')]")
            ))
            self.assertIsNotNone(modal_title)

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()