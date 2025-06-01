import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://localhost/home_page")  # Hypothetical URL used for testing

        # Step 2: Click on product category (e.g., Category A)
        try:
            category_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
            category_a.click()
        except Exception as e:
            self.fail(f"Category A link not found: {str(e)}")

        # Step 3: Select the first product (e.g., Product A)
        try:
            product_a = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
            product_a.click()
        except Exception as e:
            self.fail(f"Product A link not found: {str(e)}")

        # Step 4: Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-addtocart button")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found: {str(e)}")
        
        # Step 5: Explicitly click the cart icon to open the mini-cart
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button img[title='cart']")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found: {str(e)}")

        # Step 6: Wait for the mini-cart to become visible
        try:
            goto_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
            self.assertTrue(goto_checkout_button.is_displayed(), "GO TO CHECKOUT button is not visible")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()