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
            # Open the menu
            menu_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()

            # Navigate to the store page
            store_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()

            # Click on the first product
            product_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()

            # Select the size
            size_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button'][text()='L']"))
            )
            size_button.click()

            # Add the product to the cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()

            # Click on the cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']"))
            )
            cart_button.click()

            # Wait for the "GO TO CHECKOUT" button to be present
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
            )

            # Assert that the "GO TO CHECKOUT" button is present
            self.assertTrue(go_to_checkout_button.is_displayed())

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()