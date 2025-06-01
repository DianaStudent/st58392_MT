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
        self.driver.get("http://localhost:3000/")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20) 

        # Step 2: Click on product category
        category_a = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_a.click()

        # Step 3: Select the first product
        product_a = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_a.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.button-addtocart > button")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout'][text()='Go to checkout']")))
        
        if not go_to_checkout_button:
            self.fail("Failed: 'GO TO CHECKOUT' button not found in the mini-cart.")

if __name__ == '__main__':
    unittest.main()