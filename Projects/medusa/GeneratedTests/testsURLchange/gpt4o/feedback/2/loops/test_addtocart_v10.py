import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://localhost:8000/dk")

        try:
            # Step 1: Open the menu
            menu_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()

            # Step 2: Click the "Store" link
            store_link = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()

            # Step 3: Click on the first product image
            first_product = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a"))
            )
            first_product.click()

            # Step 4: Select the size "L"
            size_options = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[data-testid='option-button']"))
            )
            size_option_selected = False
            for size_option in size_options:
                if size_option.text == "L":
                    size_option.click()
                    size_option_selected = True
                    break
            self.assertTrue(size_option_selected, "Size option 'L' not found.")

            # Step 5: Add the product to the cart
            add_to_cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            self.assertTrue(add_to_cart_button.is_displayed(), "Add to cart button is not available.")
            add_to_cart_button.click()

            # Step 6: Click the cart button to open the cart
            cart_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
            )
            cart_button.click()

            # Step 7: Verify the presence of the "GO TO CHECKOUT" button
            checkout_button = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button']"))
            )
            self.assertTrue(checkout_button.is_displayed(), "Checkout button is not displayed.")

        except Exception as e:
            self.fail(f"Test failed due to an unexpected error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()