import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Close cookie consent if present
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception:
            self.fail("Cookie consent button not found")

        # Hover over and add the first product to the cart
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(first_product).perform()

        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Open cart popup
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Verify at least one item is in cart
        try:
            items_in_cart = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertTrue(len(items_in_cart) > 0, "No items in cart")
        except Exception:
            self.fail("Cart popup not visible or empty")

        # View cart
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Verify product in cart page
        cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area .table-content")))
        product_names = cart_items.find_elements(By.CSS_SELECTOR, ".product-name a")
        self.assertTrue(len(product_names) > 0, "No products found in cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()