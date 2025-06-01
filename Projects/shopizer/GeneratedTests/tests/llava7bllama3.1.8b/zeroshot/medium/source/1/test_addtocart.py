from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page.
        self.driver.get('http://localhost/')

        # Hover over a product image to reveal the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='product-image']"))).click()

        # Click the "Add to cart" button.
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[text()='Add to cart']")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='cart-icon']"))).click()

        # Verify that at least one product is listed in the popup cart.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//table[@class='shopping-cart-table'])[1]")))

if __name__ == '__main__':
    unittest.main()