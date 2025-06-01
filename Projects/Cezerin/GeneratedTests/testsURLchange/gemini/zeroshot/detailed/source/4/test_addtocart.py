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
        self.home_page_html = html_data["home_page"]
        self.category_a_page_html = html_data["category_a_page"]
        self.product_page_html = html_data["product_page"]
        self.popup_html = html_data["popup"]

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # 1. Open home page.
        self.assertIn("logo", self.home_page_html)

        # 2. Click on product category. (e.g. Category A)
        category_a_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        if category_a_link:
            category_a_href = category_a_link.get_attribute("href")
            category_a_link.click()
        else:
            self.fail("Category A link not found.")

        # 3. Select the first product. (e.g. Product A)
        product_a_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        if product_a_link:
            product_a_href = product_a_link.get_attribute("href")
            product_a_link.click()
        else:
            self.fail("Product A link not found.")

        # 4. Click the "Add to cart" button.
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # 5. Explicitly click the cart icon (shopping bag) to open the mini-cart.
        cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found.")

        # 6. After clicking, wait for the mini-cart to become visible.
        go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))

        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        if go_to_checkout_button:
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not visible.")
        else:
            self.fail("GO TO CHECKOUT button not found in the mini-cart.")

if __name__ == "__main__":
    unittest.main()