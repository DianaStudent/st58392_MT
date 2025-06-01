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
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to "Category A"
        try:
            category_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_a.click()
        except Exception as e:
            self.fail("Category A link not found: " + str(e))

        # Click on "Product A"
        try:
            product_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_a.click()
        except Exception as e:
            self.fail("Product A link not found: " + str(e))

        # Add to Cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button not found: " + str(e))

        # Click on cart button (shopping bag)
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
            cart_button.click()
        except Exception as e:
            self.fail("Cart button not found: " + str(e))

        # Check for "GO TO CHECKOUT" button presence
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        except Exception as e:
            self.fail("GO TO CHECKOUT button not present: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()