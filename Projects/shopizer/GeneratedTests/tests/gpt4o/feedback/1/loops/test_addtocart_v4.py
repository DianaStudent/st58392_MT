import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        accept_cookies_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookies_button.click()

        # Locate the first product and hover over it
        product_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        ActionChains(driver).move_to_element(product_element).perform()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Ensure the cart count has updated
        cart_count = self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".icon-cart .count-style"), "1")
        )

        # Click the cart icon to open the popup
        cart_icon_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon_button.click()

        # Wait for the popup to become visible
        cart_popup = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )

        # Ensure the popup is not empty
        cart_items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if not cart_items:
            self.fail("Cart popup is empty, expected at least one item.")
        
        # Click "View Cart" in the popup
        view_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
        )
        view_cart_button.click()

        # Verify the product appears in the cart list
        cart_page = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area"))
        )
        cart_items_list = cart_page.find_elements(By.CSS_SELECTOR, ".cart-table-content tbody tr")
        if not cart_items_list:
            self.fail("No items found in the cart list on the cart page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()