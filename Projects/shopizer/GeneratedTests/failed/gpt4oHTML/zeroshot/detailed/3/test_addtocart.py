from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Step 1: Open the home page
        home_page_body = self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        self.assertIsNotNone(home_page_body, "Home page is not loaded correctly.")

        # Step 2: Hover over the first product
        first_product = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img"))
        )
        ActionChains(driver).move_to_element(first_product).perform()

        # Step 3: Click the revealed "Add to cart" button.
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Step 4: Click the cart icon to open the popup cart
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # Step 5: Wait for the popup to become visible
        shopping_cart_content = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )
        self.assertIsNotNone(shopping_cart_content, "Cart popup did not appear.")

        # Step 6: Click "View cart" or similar button inside the popup
        view_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
        )
        view_cart_button.click()

        # Step 7: On the cart page, verify that the product appears in the cart list
        cart_product_name = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-name"))
        )
        self.assertTrue(cart_product_name.text.strip(), "The product is not present in the cart list.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()