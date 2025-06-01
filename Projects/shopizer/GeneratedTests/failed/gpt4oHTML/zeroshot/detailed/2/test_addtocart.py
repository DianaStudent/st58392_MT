from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Replace with your actual home page URL
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page – assumed done in setUp()

        # Step 2: Hover over the first product
        first_product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(first_product).perform()

        # Step 3: Click the revealed "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # Step 4: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Step 5: Wait for the popup to become visible
        cart_popup = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Confirm cart popup contains at least one item
        items_in_popup = cart_popup.find_elements(By.CSS_SELECTOR, ".single-shopping-cart")
        if len(items_in_popup) == 0:
            self.fail("Cart popup is empty!")

        # Step 6: Click "View cart" or similar button inside the popup
        view_cart_button = wait.until(EC.element_to_be_clickable(
            (By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 7: Verify the product appears in the cart list
        cart_page = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".cart-main-area")))
        cart_items = cart_page.find_elements(By.CSS_SELECTOR, "tbody tr")
        if len(cart_items) == 0:
            self.fail("Cart page is empty!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()