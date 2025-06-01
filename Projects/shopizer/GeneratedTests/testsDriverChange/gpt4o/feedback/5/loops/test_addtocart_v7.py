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
        except Exception as e:
            self.fail(f"Cookie consent button not found: {str(e)}")

        # Hover over the first product and add to cart
        try:
            first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(first_product).perform()

            add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Unable to add the first product to the cart: {str(e)}")

        # Open cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()

            cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content")))

            # Verify at least one item is in cart
            items_in_cart = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
            self.assertTrue(len(items_in_cart) > 0, "No items in cart")
        except Exception as e:
            self.fail(f"Cart popup not visible or empty: {str(e)}")

        # View cart
        try:
            view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "VIEW CART")))
            view_cart_button.click()

            cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-main-area .table-content")))
            product_names = cart_items.find_elements(By.CSS_SELECTOR, ".product-name a")
            self.assertTrue(len(product_names) > 0, "No products found in cart")
        except Exception as e:
            self.fail(f"Unable to verify product in cart page: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()