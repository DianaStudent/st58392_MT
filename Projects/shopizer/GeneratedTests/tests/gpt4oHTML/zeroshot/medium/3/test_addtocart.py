import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:8080")  # URL according to the HTML structure

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Hover over the first product image to reveal the "Add to cart" button
        first_product = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2 .product-img")))
        ActionChains(driver).move_to_element(first_product).perform()
        
        add_to_cart_button = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        
        if not add_to_cart_button:
            self.fail("Add to cart button is not visible")

        # 3. Click the "Add to cart" button
        add_to_cart_button.click()

        # 4. Open the cart popup by clicking the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".header-right-wrap .icon-cart")))
        
        if not cart_icon:
            self.fail("Cart icon is not clickable")
        
        cart_icon.click()

        # 5. Verify that at least one product is listed in the cart popup
        cart_popup = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content.active")))
        
        if not cart_popup:
            self.fail("Cart popup did not open properly")

        cart_items = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")

        if not cart_items:
            self.fail("No items found in the cart popup")

        self.assertTrue(len(cart_items) > 0, "Cart popup does not contain any items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()