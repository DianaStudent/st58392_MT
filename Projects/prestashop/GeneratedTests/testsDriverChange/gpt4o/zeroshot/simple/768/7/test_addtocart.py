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
        
        # Wait for Popular Products section and click on the specific product
        try:
            popular_products = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "section.featured-products h2.h2.products-section-title"))
            )
        except:
            self.fail("Popular Products section not found on the home page")

        try:
            product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='hummingbird-printed-t-shirt']"))
            )
            product.click()
        except:
            self.fail("Product link not found or not clickable")

        # Verify product detail page and click Add to Cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to Cart button not found or not clickable")
        
        # Wait for and verify modal confirmation
        try:
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#blockcart-modal h4"))
            )
            self.assertIn("successfully added", modal.text.lower())
        except:
            self.fail("Confirmation modal not found or verification failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()