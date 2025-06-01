from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost/")  # Assuming localhost for testing

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies if the button is present
        try:
            accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_btn.click()
        except:
            pass  # If there's no consent button, move on.

        # Hover over the first product to reveal the add to cart button
        action = ActionChains(driver)
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2.mb-25")))
        action.move_to_element(first_product).perform()

        # Click "Add to cart" on the first product
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 > button[title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the cart popup
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for the cart popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Check if the cart popup contains at least one item
        items_in_cart = driver.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if len(items_in_cart) == 0:
            self.fail("No items found in the cart popup.")

        # Click "View Cart" inside the cart popup
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # Verify the product appears in the cart list
        cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cart-main-area .product-name")))
        if not cart_items:
            self.fail("Cart items not found.")
        
        self.assertTrue(any("Chair" in item.text or "Olive Table" in item.text for item in cart_items), "Product not found in cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()