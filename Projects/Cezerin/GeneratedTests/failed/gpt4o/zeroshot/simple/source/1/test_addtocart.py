from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Category A page
        category_a = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a.click()

        # Select Product A
        product_a = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_a.click()

        # Add to cart
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
        )
        add_to_cart_button.click()

        # Click on cart button (shopping bag)
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_button.click()

        # Verify presence of "GO TO CHECKOUT" button
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'GO TO CHECKOUT')]"))
        )

        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()