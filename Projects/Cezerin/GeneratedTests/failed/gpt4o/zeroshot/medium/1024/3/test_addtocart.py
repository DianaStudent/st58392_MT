from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click on Category A
        category_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Select the first product
        product_a = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Click "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-addtocart') and contains(@class, 'is-success')]")))
        add_to_cart_button.click()
        
        # Click cart icon to open mini-cart
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'cart-button')]")))
        cart_button.click()

        # Verify "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/checkout' and contains(text(), 'GO TO CHECKOUT')]")))
            self.assertTrue(go_to_checkout_button.is_displayed())
        except Exception as e:
            self.fail("GO TO CHECKOUT button not found in the cart: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()