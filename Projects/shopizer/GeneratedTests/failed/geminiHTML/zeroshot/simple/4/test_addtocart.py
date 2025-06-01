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
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )
        
        # Find the add to cart button within the product element
        add_to_cart_button = product_element.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        
        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(add_to_cart_button)
            ).click()
        except Exception as e:
            self.fail(f"Could not click 'Add to cart' button: {e}")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .cart-wrap .icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Could not click cart icon: {e}")

        # Confirm success by checking that the popup contains at least one item
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active .single-shopping-cart"))
            )
        except Exception as e:
            self.fail(f"Cart popup does not contain any items: {e}")


if __name__ == "__main__":
    unittest.main()