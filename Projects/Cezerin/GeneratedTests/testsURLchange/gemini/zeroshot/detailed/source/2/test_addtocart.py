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
        home_page_html = self.html_data["home_page"]
        category_a_page_html = self.html_data["category_a_page"]
        product_page_html = self.html_data["product_page"]
        popup_html = self.html_data["popup"]

        # 1. Open home page.
        # Home page is already opened in setUp()

        # 2. Click on product category. (e.g. Category A)
        category_a_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found on home page.")

        # 3. Select the first product. (e.g. Product A)
        product_a_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found on category page.")

        # 4. Click the "Add to cart" button.
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found on product page.")

        # 5. Explicitly click the cart icon (shopping bag) to open the mini-cart.
        cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found.")

        # 6. After clicking, wait for the mini-cart to become visible.
        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]")))
        if go_to_checkout_button:
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed.")
        else:
            self.fail("Go to checkout button not found in mini-cart.")
if __name__ == "__main__":
    unittest.main()