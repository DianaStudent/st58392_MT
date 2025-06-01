from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get("http://localhost/")

        # Step 2: Hover over the first product to reveal "Add to cart"
        product_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(product_element).perform()

        # Step 3: Click the revealed "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart")))
        cart_icon.click()

        # Step 5: Wait for the popup to become visible
        popup_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        
        # Check that the popup contains at least one item
        cart_items = popup_cart.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not cart_items:
            self.fail("No items found in the cart popup.")

        # Step 6: Click "View cart" button inside the popup
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 7: On the cart page, verify that the product appears in the cart list
        cart_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area")))
        
        cart_items_page = cart_page.find_elements(By.CSS_SELECTOR, ".product-name a")
        if not cart_items_page:
            self.fail("No products found in the cart page.")
        
        expected_product_name = "Chair"  # Expected product name based on initial cart addition
        product_names = [item.text for item in cart_items_page]
        self.assertIn(expected_product_name, product_names, f"{expected_product_name} not found in cart page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()