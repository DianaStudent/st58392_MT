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
        try:
            # Open Menu
            nav_menu_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            nav_menu_button.click()

            # Go to Store page
            store_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()

            # Click on the first product
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()

            # Select size
            size_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='L']"))
            )
            size_button.click()

            # Add to cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()

            # Click on cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
            )
            cart_button.click()

            # Check for "Go to checkout" button
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button"))
            )

            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed")

        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()