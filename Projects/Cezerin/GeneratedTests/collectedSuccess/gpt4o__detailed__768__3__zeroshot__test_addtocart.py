import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on Category A
        category_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # Step 3: Select the first product (Product A)
        product_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_btn.click()

        # Step 5: Click on the cart icon to open the mini-cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button img[title='cart']")))
        cart_button.click()

        # Step 6: Wait for the mini-cart to become visible
        go_to_checkout_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))

        # Step 7: Verify the "GO TO CHECKOUT" button is present
        if not go_to_checkout_btn or not go_to_checkout_btn.is_displayed():
            self.fail("GO TO CHECKOUT button is not visible or present in the mini-cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()