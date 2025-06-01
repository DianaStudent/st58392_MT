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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies banner if present
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Cookies accept button not found or not clickable.")

        # Hover over the first product to reveal the "Add to cart" button
        try:
            product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
            ActionChains(driver).move_to_element(product).perform()
        except:
            self.fail("Product image not found or not hoverable.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='product-action-2']/button[@title='Add to cart']")
                )
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable.")
        
        # Click the cart icon to open the cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable.")

        # Verify that the cart popup contains at least one item
        try:
            cart_items = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content ul li.single-shopping-cart"))
            )
            self.assertIsNotNone(cart_items, "Cart popup does not contain any items.")
        except:
            self.fail("Cart popup does not contain any items or is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()