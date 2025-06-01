```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        url = "http://localhost:3000/"
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())
        self.wait_time = 20

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        # Open home page
        self.driver.get(url)

        # Click on product category
        self.product_category_link = WebDriverWait(self.driver, self.wait_time).until(
            By.XPATH, "//a[@href='category']");
        self.product_category_link.click()

        # Select the first product
        self.first_product = WebDriverWait(self.driver, self.wait_time).until(
            By.XPATH, "//li/a[@class='product-link']");
        self.first_product.click()

        # Click the  "Add to cart" button
        self.add_to_cart_button = WebDriverWait(self.driver, self.wait_time).until(
            By.XPATH, "//button[@id='add-to-cart-btn']");
        self.add_to_cart_button.click()

        # Open the shopping bag
        self.cart_icon = WebDriverWait(self.driver, self.wait_time).until(
            By.XPATH, "//span[@class='cart-button']");
        self.cart_icon.click()

        # Verify that the  "GO TO CHECKOUT" button is present inside the cart
        self.go_to_checkout_button = WebDriverWait(self.driver, self.wait_time).until(
            By.XPATH, "//button[@id='go-to-checkout-btn']");
        self.assertEqual(self.go_to_checkout_button.get_attribute("id"), "go-to-checkout-btn")

if __name__ == "__main__":
    unittest.main()
```