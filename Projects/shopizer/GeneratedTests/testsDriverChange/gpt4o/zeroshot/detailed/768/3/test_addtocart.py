from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)

        # Hover over the first product to reveal the "Add to cart" button
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        actions.move_to_element(first_product).perform()

        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2 .product-action-2 button[title='Add to cart']")))
        actions.move_to_element(add_to_cart_button).click().perform()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for popup to become visible
        popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Click "View cart" inside the popup
        view_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content a[href='/cart']")))
        view_cart_button.click()

        # Verify that the product appears in the cart list
        cart_page_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-page-title")))
        self.assertTrue(cart_page_title.is_displayed(), "Cart page title not found.")

        product_in_cart = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table-content .product-name a")))
        self.assertTrue(product_in_cart.is_displayed(), "Expected product not found in cart.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()