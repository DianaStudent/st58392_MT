import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        actions = ActionChains(driver)

        # Hover over the first product to reveal the "Add to cart" button
        product_locator = (By.CSS_SELECTOR, "div.product-wrap-2")
        wait.until(EC.presence_of_element_located(product_locator))
        first_product = driver.find_element(*product_locator)
        
        actions.move_to_element(first_product).perform()

        # Click the revealed "Add to cart" button
        add_to_cart_btn_locator = (By.CSS_SELECTOR, "button[title='Add to cart']")
        wait.until(EC.presence_of_element_located(add_to_cart_btn_locator))
        add_to_cart_button = driver.find_element(*add_to_cart_btn_locator)
        self.assertTrue(add_to_cart_button is not None and add_to_cart_button.is_displayed(), "Add to cart button is not found")
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CSS_SELECTOR, "button.icon-cart")
        wait.until(EC.presence_of_element_located(cart_icon_locator))
        cart_icon = driver.find_element(*cart_icon_locator)
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup_locator = (By.CSS_SELECTOR, "div.shopping-cart-content")
        wait.until(EC.visibility_of_element_located(cart_popup_locator))
        cart_popup = driver.find_element(*cart_popup_locator)
        self.assertTrue(cart_popup is not None and len(cart_popup.text) > 0, "Cart popup is not visible or empty")

        # Click "View cart" or similar button inside the popup
        view_cart_btn_locator = (By.CSS_SELECTOR, "a[href='/cart']")
        wait.until(EC.presence_of_element_located(view_cart_btn_locator))
        view_cart_button = driver.find_element(*view_cart_btn_locator)
        self.assertTrue(view_cart_button is not None and view_cart_button.is_displayed(), "View Cart button is not found")
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_page_locator = (By.CSS_SELECTOR, "table.cart-table-content")
        wait.until(EC.presence_of_element_located(cart_page_locator))
        cart_table = driver.find_element(*cart_page_locator)
        self.assertTrue(cart_table is not None and len(cart_table.text) > 0, "Cart table is not visible or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()