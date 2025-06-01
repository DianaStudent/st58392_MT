import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_add_to_cart(self):
        # Navigate to the home page
        self.driver.get("http://localhost:3000/")

        # Click on product category "Category A"
        category_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_button.click()

        # Select the first product "Product A"
        product_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//h2[@class='product-title']/following-sibling::*)[1]")))
        product_title.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='add-to-cart']")))
        add_to_cart_button.click()

        # Explicitly click the shopping cart icon (shopping bag) to open the mini-cart
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='cart-button']")))
        cart_icon.click()

        # Wait for the mini-cart to become visible
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-cart']")))

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//button)[1]")))
        self.assertIsNotNone(checkout_button)
        self.assertEqual("GO TO CHECKOUT", checkout_button.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()