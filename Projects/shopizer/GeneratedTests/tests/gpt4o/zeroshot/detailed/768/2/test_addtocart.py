import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):

        # Accept cookies if the consent button is present
        try:
            consent_button = self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            if consent_button:
                consent_button.click()
        except:
            pass

        # Step 2: Hover over the first product to reveal "Add to cart" button
        product_img_locator = (By.CSS_SELECTOR, ".product-wrap-2 .product-img")
        product_img = self.wait.until(EC.presence_of_element_located(product_img_locator))
        
        ActionChains(self.driver).move_to_element(product_img).perform()

        # Step 3: Click "Add to cart" button
        add_to_cart_button_locator = (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        add_to_cart_button = self.wait.until(EC.presence_of_element_located(add_to_cart_button_locator))

        if not add_to_cart_button:
            self.fail("Add to cart button not found or not revealed.")

        add_to_cart_button.click()

        # Step 4: Click on the cart icon
        cart_icon_locator = (By.CSS_SELECTOR, ".icon-cart > i.pe-7s-shopbag")
        cart_icon = self.wait.until(EC.presence_of_element_located(cart_icon_locator))
        
        if not cart_icon:
            self.fail("Cart icon not found.")
        
        cart_icon.click()

        # Step 5: Wait for the popup cart to become visible
        cart_popup_locator = (By.CSS_SELECTOR, ".shopping-cart-content.active")
        cart_popup = self.wait.until(EC.visibility_of_element_located(cart_popup_locator))

        if not cart_popup:
            self.fail("Cart popup did not become visible.")

        # Step 6: Click the "View Cart" button
        view_cart_button_locator = (By.XPATH, "//a[contains(text(),'View Cart')]")
        view_cart_button = self.wait.until(EC.presence_of_element_located(view_cart_button_locator))
        
        if not view_cart_button:
            self.fail("View Cart button not found in the cart popup.")
        
        view_cart_button.click()

        # Step 7: Verify the product appears in the cart list
        cart_item_locator = (By.XPATH, "//h4/a[text()='Chair']")
        cart_items = self.wait.until(EC.presence_of_element_located(cart_item_locator))
        
        if not cart_items:
            self.fail("Product not found in the cart list.")
        
        self.assertTrue(cart_items, "The product does not appear in the cart list.")

if __name__ == "__main__":
    unittest.main()