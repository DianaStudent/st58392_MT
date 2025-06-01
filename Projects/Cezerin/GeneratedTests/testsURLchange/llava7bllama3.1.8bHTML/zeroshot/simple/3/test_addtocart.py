from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/')

    def test_add_to_cart(self):
        # Navigate to product page and click add to cart button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-name'))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button-addtocart button'))).click()

        # Wait for presence of cart button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.cart'))).click()

        # Wait for presence of "GO TO CHECKOUT" button using html_data
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.product-name + .button-addtocart')))
            self.fail("Expected element not found")
        except TimeoutException:
            pass

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()