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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://localhost/")

        # Accept cookies
        accept_cookies_btn = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_btn.click()
        
        # Locate the first product item and hover over it to reveal "Add to cart" button
        product_item = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        add_to_cart_button = product_item.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        ActionChains(driver).move_to_element(product_item).perform()

        # Click "Add to cart" button
        add_to_cart_button.click()

        # Open the cart popup by clicking on the cart icon
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
        cart_icon.click()

        # Verify that the popup contains at least one item
        shopping_cart_content = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        items = shopping_cart_content.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        
        if not items:
            self.fail("Cart does not contain any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()