import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Ensure the home page is open
        home_url = driver.current_url
        self.assertEqual(home_url, "http://localhost:3000/")

        # 2. Click on Category A
        try:
            category_a_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()
        except TimeoutException:
            self.fail("Failed to find or click on the category link.")

        # 3. Select the first product (Product A)
        try:
            product_a_link = wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except TimeoutException:
            self.fail("Failed to find or click on the product link.")

        # 4. Click "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Failed to find or click on the add to cart button.")

        # 5. Click on the cart icon/button to open the mini-cart
        try:
            cart_button = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
            )
            cart_button.click()
        except TimeoutException:
            self.fail("Failed to find or click on the cart button.")

        # 6. Verify that the "GO TO CHECKOUT" button is inside the mini-cart
        try:
            go_to_checkout_button = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//a[@class='button is-primary is-fullwidth has-text-centered' and normalize-space()='Go to checkout']")
                )
            )
            self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button is not present in the mini-cart.")
        except TimeoutException:
            self.fail("GO TO CHECKOUT button is not found or appeared timely.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()