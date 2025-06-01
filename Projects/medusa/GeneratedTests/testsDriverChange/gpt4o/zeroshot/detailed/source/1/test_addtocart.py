import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Click the menu button ("Menu").
        menu_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']"))
        )
        menu_button.click()

        # Click the "Store" link.
        store_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']"))
        )
        store_link.click()

        # Click on a product image (Thumbnail) - first product.
        product_thumbnail = wait.until(
            EC.presence_of_element_located((By.XPATH, "(//ul[@data-testid='products-list']/li/a)[1]"))
        )
        product_thumbnail.click()

        # Select size by clicking the size button "L".
        size_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button' and text()='L']"))
        )
        size_button.click()

        # Add the product to the cart.
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']"))
        )
        add_to_cart_button.click()

        # Explicitly click the cart button to open the cart.
        cart_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']"))
        )
        cart_link.click()

        # Verify that the "GO TO CHECKOUT" button is present.
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-testid='checkout-button']/button"))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button was not found.")

if __name__ == "__main__":
    unittest.main()