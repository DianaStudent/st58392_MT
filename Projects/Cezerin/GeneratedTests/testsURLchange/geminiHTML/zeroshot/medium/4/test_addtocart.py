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
        # 1. Open home page.
        home_page_html = self.driver.page_source
        self.assertTrue(home_page_html, "Home page is empty.")

        # 2. Click on product category.
        category_a_link = self.driver.find_element(By.XPATH, "//a[@href='/category-a']")
        self.assertIsNotNone(category_a_link, "Category A link not found.")
        category_a_link.click()

        # 3. Select the first product.
        product_a_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
        )
        self.assertIsNotNone(product_a_link, "Product A link not found.")
        product_a_link.click()

        # 4. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']"))
        )
        self.assertIsNotNone(add_to_cart_button, "Add to cart button not found.")
        add_to_cart_button.click()

        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart-button"))
        )
        self.assertIsNotNone(cart_button, "Cart button not found.")
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout' and contains(text(), 'Go to checkout')]"))
        )
        self.assertIsNotNone(go_to_checkout_button, "Go to checkout button not found.")

if __name__ == "__main__":
    unittest.main()