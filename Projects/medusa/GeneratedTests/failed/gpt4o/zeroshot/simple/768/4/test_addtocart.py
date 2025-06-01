from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Click on the menu button
            menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            menu_button.click()

            # Click on the store link in the menu
            store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()

            # Click on the first product in the store page
            first_product = wait.until(EC.element_to_be_clickable((By.XPATH, "(//a[contains(@href, '/dk/products/')])[1]")))
            first_product.click()

            # Select a size
            size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-testid='product-options']/button[text()='L']")))
            size_button.click()

            # Add to cart
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()

            # Open cart
            cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
            cart_link.click()

            # Verify "GO TO CHECKOUT" button is visible
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button']>button")))
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()