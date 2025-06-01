from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Category A"
        category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_link.click()

        # Select the first product link
        first_product_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        first_product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'button-addtocart')]//button[text()='Add to cart']"))
        )
        add_to_cart_button.click()

        # Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout']"))
        )
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()