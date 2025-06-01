import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Navigate to Category A
            category_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()

            # Select Product A
            product_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()

            # Add Product A to cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()

            # Click on the cart button (shopping bag)
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']"))
            )
            cart_button.click()

            # Verify the "GO TO CHECKOUT" button is present
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout'][contains(text(), 'Go to checkout')]"))
            )

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()