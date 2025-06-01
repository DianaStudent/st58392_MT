import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver

        # Click on Category A (by href)
        category_a = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a.click()

        # Click on the first product (link by href)
        first_product = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        first_product.click()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button-addtocart')]"))
        )
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-button']"))
        )
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout' and contains(@class, 'button is-primary')]"))
        )

        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found in the cart")

# Execute the test class if this module is run directly
if __name__ == "__main__":
    unittest.main()