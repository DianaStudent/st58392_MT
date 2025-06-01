import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

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
        category_a_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
        )
        category_a_link.click()

        # 3. Select the first product (Product A)
        product_a_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        product_a_link.click()

        # 4. Click "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
        )
        add_to_cart_button.click()

        # 5. Click on cart icon/button to open the mini-cart
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button"))
        )
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is inside the mini-cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@class, 'button') and text()='GO TO CHECKOUT']")
            )
        )
        
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present in the mini-cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()