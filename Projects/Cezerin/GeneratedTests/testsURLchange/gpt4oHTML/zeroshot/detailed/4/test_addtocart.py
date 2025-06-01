import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("data:text/html;charset=utf-8," + html_data["home_page"])

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on product category (Category A)
        category_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # Ensure Category A page is loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a-1']")))

        # Step 3: Select the first product (Product A)
        product_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # Ensure Product page is loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-name")))

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart .button")))
        add_to_cart_button.click()

        # Step 5: Explicitly click the cart icon
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # Step 6: Wait for the mini-cart to become visible
        mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".mini-cart-open")))

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary")))

        if not (go_to_checkout_button and go_to_checkout_button.is_displayed()):
            self.fail("GO TO CHECKOUT button is not present or not visible in the mini-cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()