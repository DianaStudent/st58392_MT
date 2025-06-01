import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the first product wrap
        product_wrap = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )

        # Hover over the product to reveal the "Add to cart" button
        actions = ActionChains(driver)
        actions.move_to_element(product_wrap).perform()

        # Find and click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Open the cart popup
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable")

        # Check if the cart popup is opened and contains at least one item
        try:
            cart_items = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".shopping-cart-content ul li.single-shopping-cart"))
            )
            self.assertTrue(len(cart_items) > 0, "Cart is empty")
        except:
            self.fail("Cart items not found in the popup")


if __name__ == "__main__":
    unittest.main()