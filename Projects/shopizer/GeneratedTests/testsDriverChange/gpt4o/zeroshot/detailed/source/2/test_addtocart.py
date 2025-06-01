import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        actions = ActionChains(driver)

        # Accept cookies
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except:
            self.fail("Cookies accept button not found")

        # Hover over the first product
        try:
            first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            actions.move_to_element(first_product).perform()
        except:
            self.fail("First product not found")

        # Click "Add to cart"
        try:
            add_to_cart_button = wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not available")

        # Open cart popup
        try:
            cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found")

        # Wait for popup
        try:
            pop_up_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        except:
            self.fail("Cart popup not visible")

        # Click "View Cart" button
        try:
            view_cart_button = pop_up_cart.find_element(By.LINK_TEXT, "View Cart")
            view_cart_button.click()
        except:
            self.fail("View cart button not found in popup")

        # Check cart page for product
        try:
            cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-table-content tbody")))
            cart_item_list = cart_items.find_elements(By.CSS_SELECTOR, "tr")
            self.assertGreater(len(cart_item_list), 0, "Cart is empty, no items found")
        except:
            self.fail("Cart items not found on cart page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()