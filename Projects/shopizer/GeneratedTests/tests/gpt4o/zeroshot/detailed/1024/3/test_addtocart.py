import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost/")

        wait = WebDriverWait(driver, 20)

        # Step 2: Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.product-wrap-2')))
        ActionChains(driver).move_to_element(first_product).perform()

        # Step 3: Click the revealed "Add to cart" button
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, 'button[title="Add to cart"]')
        add_to_cart_button.click()

        # Step 4: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.icon-cart')))
        cart_icon.click()

        # Step 5: Wait for the popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.shopping-cart-content.active')))
        self.assertTrue(cart_popup.is_displayed(), msg="Cart popup is not displayed.")

        # Step 6: Click "View cart" button inside the popup
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, 'VIEW CART')
        view_cart_button.click()

        # Step 7: On the cart page, verify that the product appears in the cart list
        cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'table.cart-table-content')))
        
        items = cart_items.find_elements(By.CSS_SELECTOR, 'tr')
        self.assertTrue(len(items) > 0, msg="No items found in the cart.")

    def tearDown(self):
        # Tear down the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()