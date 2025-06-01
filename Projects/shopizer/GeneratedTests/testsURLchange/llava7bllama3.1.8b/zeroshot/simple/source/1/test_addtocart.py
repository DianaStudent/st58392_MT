import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_add_to_cart(self):
        # Wait for product item to load
        product_item = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='products list-unstyled']/li[1]")))

        # Hover over the product item
        self.driver.execute_script("arguments[0].hover();", product_item)

        # Wait for Add to cart button to be visible and clickable
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='products list-unstyled']/li[1]//button[text()='Add to Cart']")))

        # Click the Add to cart button
        add_to_cart_button.click()

        # Wait for cart popup to load
        cart_popup = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cart']")))

        # Check if the cart contains at least one item
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.XPATH, "//span[@class='cart-title']", 'Your Cart'))))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()