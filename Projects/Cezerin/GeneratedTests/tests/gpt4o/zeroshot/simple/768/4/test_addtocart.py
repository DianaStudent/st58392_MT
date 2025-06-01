import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Category A
        try:
            category_a = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/category-a']")))
            category_a.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Category A: {str(e)}")

        # Click on Product A
        try:
            product_a = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/category-a/product-a']")))
            product_a.click()
        except Exception as e:
            self.fail(f"Failed to click on Product A: {str(e)}")

        # Click on Add to Cart button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(., 'Add to cart')]")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add Product A to cart: {str(e)}")

        # Click on Cart button
        try:
            cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//span[@class='cart-button']/img")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Failed to open the cart: {str(e)}")

        # Verify "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[contains(., 'GO TO CHECKOUT')]")))
        except Exception as e:
            self.fail(f"'GO TO CHECKOUT' button is not present: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()