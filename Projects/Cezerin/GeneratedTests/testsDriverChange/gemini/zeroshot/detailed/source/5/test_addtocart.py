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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        home_page_html = self.driver.page_source
        category_a_href = None
        product_a_href = None

        # 1. Open home page.
        self.assertIn("<div id=\"app\">", home_page_html, "Home page not loaded correctly.")

        # 2. Click on product category. (e.g. Category A)
        try:
            category_a_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            category_a_href = category_a_element.get_attribute("href")
            category_a_element.click()
        except Exception as e:
            self.fail(f"Could not click on Category A: {e}")

        # 3. Select the first product. (e.g. Product A)
        try:
            product_a_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
            product_a_href = product_a_element.get_attribute("href")
            product_a_element.click()
        except Exception as e:
            self.fail(f"Could not click on Product A: {e}")

        # 4. Click the "Add to cart" button.
        try:
            add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on Add to cart button: {e}")

        # 5. Explicitly click the cart icon (shopping bag) to open the mini-cart.
        try:
            cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not click on cart button: {e}")

        # 6. After clicking, wait for the mini-cart to become visible.
        try:
            go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]")))
        except Exception as e:
            self.fail(f"Mini-cart did not become visible or 'Go to checkout' button not found: {e}")

        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")

if __name__ == "__main__":
    unittest.main()