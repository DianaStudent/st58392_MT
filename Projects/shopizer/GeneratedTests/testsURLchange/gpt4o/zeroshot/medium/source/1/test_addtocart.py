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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        actions = ActionChains(driver)

        # Accept cookies
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except Exception as e:
            self.fail("Cookie acceptance button not found: {}".format(e))

        # Hover over a product image to reveal the "Add to cart" button
        try:
            product_image = self.wait.until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2 .product-img")
            ))
            actions.move_to_element(product_image).perform()
        except Exception as e:
            self.fail("Product image not found: {}".format(e))

        # Click the "Add to cart" button
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            ))
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button not found: {}".format(e))

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".icon-cart")
            ))
            cart_icon.click()
        except Exception as e:
            self.fail("Cart icon not found: {}".format(e))

        # Verify that at least one product is listed in the popup cart
        try:
            cart_items = self.wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".single-shopping-cart")
            ))
            if not cart_items:
                self.fail("No items found in the cart popup")
        except Exception as e:
            self.fail("Cart popup items not found: {}".format(e))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()