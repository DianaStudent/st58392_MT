from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page.
        self.driver.get('http://localhost/')

        # Hover over a product image to reveal the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//img[@class='product-image']"))).click()

        # Click the "Add to cart" button.
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-icon']"))).click()

        # Verify that at least one product is listed in the popup cart.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//table[@class='shopping-cart-table'])[1]")))

if __name__ == '__main__':
    unittest.main()