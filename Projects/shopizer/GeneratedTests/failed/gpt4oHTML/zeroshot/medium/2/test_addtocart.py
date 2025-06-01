from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Assuming this is the base URL for the local server
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait
        actions = ActionChains(driver)
        
        # Step 1: Navigate to home page (already done in setUp)

        # Step 2: Hover over the first product to reveal the "Add to cart" button
        product_img_selector = (By.CSS_SELECTOR, ".product-img")
        product_img_element = wait.until(EC.visibility_of_element_located(product_img_selector))
        
        if not product_img_element:
            self.fail("Product image not found.")

        actions.move_to_element(product_img_element).perform()

        # Step 3: Click the "Add to cart" button
        add_to_cart_button_selector = (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_button_selector))
        
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")

        add_to_cart_button.click()

        # Step 4: Open the cart popup by clicking the cart icon
        cart_icon_selector = (By.CSS_SELECTOR, ".header-right-wrap .icon-cart")
        cart_icon = wait.until(EC.element_to_be_clickable(cart_icon_selector))

        if not cart_icon:
            self.fail("Cart icon not found.")

        cart_icon.click()

        # Step 5: Verify that at least one product is listed in the cart popup
        cart_popup_selector = (By.CSS_SELECTOR, ".shopping-cart-content.active")
        cart_popup = wait.until(EC.visibility_of_element_located(cart_popup_selector))

        if not cart_popup:
            self.fail("Cart popup is not displayed.")

        product_list_selector = (By.CSS_SELECTOR, ".shopping-cart-content.active ul li.single-shopping-cart")
        products = cart_popup.find_elements(*product_list_selector)

        if not products:
            self.fail("No products found in cart popup.")

        # Assert that there is at least one product in the cart popup
        self.assertTrue(len(products) > 0, "No product found in cart popup.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()