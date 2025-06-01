import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for the page to load by checking an element
        root_element = wait.until(EC.presence_of_element_located((By.ID, "root")))

        # Hover over the first product to reveal "Add to cart" button
        first_product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2 .product-action-2 button[title='Add to cart']")
        ))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-wrap-2 .product-action-2 button[title='Add to cart']")
        ))
        if not add_to_cart_button:
            self.fail("Add to cart button not found or not clickable.")
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".icon-cart")
        ))
        if not cart_icon:
            self.fail("Cart icon not found or not clickable.")
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content.active")
        ))
        if not cart_popup:
            self.fail("Cart popup did not become visible.")

        # Click "View Cart" inside the popup
        view_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".shopping-cart-content.active a[href='/cart']")
        ))
        if not view_cart_button:
            self.fail("View cart button not found in cart popup.")
        view_cart_button.click()

        # Verify that the product appears in the cart list
        product_in_cart = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//td[@class='product-name']/a[text()='Chair']")
        ))
        if not product_in_cart:
            self.fail("Product not found in cart list.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()