from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Find and click the "Store" link
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Store"))
            )
            store_link.click()
        except:
            self.fail("Could not find or click the 'Store' link.")

        # Find and click the first product link
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//ul[@data-testid='products-list']/li[1]/a"))
            )
            product_link.click()
        except:
            self.fail("Could not find or click the first product link.")

       # Select size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='product-options']/button[1]"))
            )
            size_button.click()
        except:
            self.fail("Could not find or click the size button.")

        # Find and click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button.")

        # Find and click the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

        # Wait for presence of "GO TO CHECKOUT" button
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='checkout-button']/button"))
            )
        except:
            self.fail("Could not find 'GO TO CHECKOUT' button after adding product to cart.")

if __name__ == "__main__":
    unittest.main()