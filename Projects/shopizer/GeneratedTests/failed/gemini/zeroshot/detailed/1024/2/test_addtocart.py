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

        # Accept cookies
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")))
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the cart popup
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content.active")))

        # Check that the popup contains at least one item
        cart_items = cart_popup.find_elements(By.CLASS_NAME, "single-shopping-cart")
        if not cart_items:
            self.fail("Cart is empty after adding a product")

        # Click "View Cart" button
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_page_product_name = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-page-title")))
        if not cart_page_product_name.text:
            self.fail("Cart page title is missing")

        product_name_element = wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='product-name']/a")))
        if not product_name_element.text:
             self.fail("Product name is missing from cart page")

if __name__ == "__main__":
    unittest.main()