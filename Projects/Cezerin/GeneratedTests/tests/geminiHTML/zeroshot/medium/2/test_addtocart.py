import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        home_page_html = self.driver.page_source
        if not home_page_html:
            self.fail("Home page is empty.")

        # 1. Click on product category.
        category_a_link = self.driver.find_element(By.XPATH, "//a[@href='/category-a']")
        if not category_a_link:
            self.fail("Category A link not found.")
        category_a_link.click()

        # 2. Select the first product.
        product_a_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        if not product_a_link:
            self.fail("Product A link not found.")
        product_a_link.click()

        # 3. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()

        # 4. Click the cart icon/button to open the shopping bag.
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
        )
        if not cart_button:
            self.fail("Cart button not found.")
        cart_button.click()

        # 5. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/checkout') and contains(@class, 'is-primary') and contains(text(), 'Go to checkout')]"))
        )
        if not go_to_checkout_button:
            self.fail("Go to checkout button not found in the cart.")

if __name__ == "__main__":
    unittest.main()