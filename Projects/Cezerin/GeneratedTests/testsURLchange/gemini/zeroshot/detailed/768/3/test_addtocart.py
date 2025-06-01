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
        category_a_href = "/category-a"
        product_a_href = "/category-a/product-a"

        # 1. Open home page - Already done in setUp

        # 2. Click on product category (Category A)
        category_a_link = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{category_a_href}']")))
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found.")

        # 3. Select the first product (Product A)
        product_a_link = self.wait.until(EC.presence_of_element_located((By.XPATH, f"//a[@href='{product_a_href}']")))
        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found.")

        # 4. Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Explicitly click the cart icon (shopping bag)
        cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found.")

        # 6. Wait for the mini-cart to become visible
        checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]")))

        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        if checkout_button:
            self.assertTrue(checkout_button.is_displayed(), "Checkout button is not displayed.")
        else:
            self.fail("Checkout button not found in mini-cart.")

if __name__ == "__main__":
    unittest.main()