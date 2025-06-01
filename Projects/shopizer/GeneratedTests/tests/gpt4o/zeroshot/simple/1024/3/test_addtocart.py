from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
    
    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Close cookie consent if present
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
        except Exception as e:
            self.fail(f"Cookie consent not closed: {str(e)}")

        try:
            # Hover over "Olive Table" product to reveal "Add to cart" button
            product_hover = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-img']/a[@href='/product/olive-table']"))
            )
            webdriver.ActionChains(driver).move_to_element(product_hover).perform()
            
            # Click "Add to cart" for Olive Table
            add_to_cart_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-action-2']//button[@title='Add to cart']"))
            )
            add_to_cart_btn.click()
        except Exception as e:
            self.fail(f"Add to Cart operation failed: {str(e)}")

        try:
            # Open cart popup by clicking the cart icon
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='header-right-wrap']//button[@class='icon-cart']"))
            )
            cart_icon.click()

            # Check if cart popup contains at least one item
            cart_items = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'shopping-cart-content')]//li[@class='single-shopping-cart']"))
            )

            self.assertIsNotNone(cart_items, "No items are present in the cart")
        except Exception as e:
            self.fail(f"Cart verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()