import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.driver.set_window_size(1024, 768)

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)

        # Accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if accept_cookies_button:
                accept_cookies_button.click()
        except:
            self.fail("Cookie accept button not found.")

        # Hover over the first product to reveal the "Add to cart" button
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        if product:
            action.move_to_element(product).perform()
        else:
            self.fail("First product not found.")

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found.")

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
        if cart_icon:
            cart_icon.click()
        else:
            self.fail("Cart icon not found.")

        # Wait for the cart popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        if not cart_popup or "No items added to cart" in cart_popup.text:
            self.fail("Popup cart did not become visible or is empty.")

        # Click "View Cart" in the popup
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        if view_cart_button:
            view_cart_button.click()
        else:
            self.fail("View Cart button in popup not found.")

        # Verify product appears in the cart list
        cart_table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content table")))
        if cart_table:
            rows = cart_table.find_elements(By.TAG_NAME, "tr")
            self.assertTrue(len(rows) > 0, "No items found in cart.")
        else:
            self.fail("Cart table not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()