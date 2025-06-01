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
        if not home_page_html:
            self.fail("Home page is empty.")

        # 1. Click on Category A
        category_a_link = self.driver.find_element(By.XPATH, "//a[@href='/category-a']")
        if not category_a_link:
            self.fail("Category A link not found.")
        category_a_link.click()

        # 2. Select the first product (Product A)
        product_a_link = self.driver.find_element(By.XPATH, "//a[@href='/category-a/product-a']")
        if not product_a_link:
            self.fail("Product A link not found.")
        product_a_link.click()

        # 3. Click the "Add to cart" button
        add_to_cart_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]")
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()

        # 4. Explicitly click the cart icon (shopping bag)
        cart_button = self.driver.find_element(By.XPATH, "//span[@class='cart-button']")
        if not cart_button:
            self.fail("Cart button not found.")
        cart_button.click()

        # 5. Wait for the mini-cart to become visible and Verify that the "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not visible.")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found or not visible: {e}")

if __name__ == "__main__":
    unittest.main()