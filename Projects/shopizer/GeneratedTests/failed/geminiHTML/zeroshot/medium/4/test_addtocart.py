from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # Accept cookies if the consent banner is present
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )
        if product_element is None:
            self.fail("Product element not found")

        action = ActionChains(driver)
        action.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        if add_to_cart_button is None:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )
        if cart_icon is None:
            self.fail("Cart icon not found")
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        cart_items = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".shopping-cart-content ul li.single-shopping-cart"))
        )

        if not cart_items:
            self.fail("No items found in the cart popup")
        
        self.assertTrue(len(cart_items) > 0, "No items found in cart popup")


if __name__ == "__main__":
    unittest.main()