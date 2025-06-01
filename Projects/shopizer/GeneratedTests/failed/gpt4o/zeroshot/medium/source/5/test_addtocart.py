from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Wait for the page to load and accept cookies
        cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()

        # Locate the product item and hover over it
        product_img = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-img")))
        ActionChains(driver).move_to_element(product_img).perform()

        # Click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the cart popup
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart")))
        cart_icon.click()

        # Check that the cart popup is opened with at least one product
        cart_content = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.shopping-cart-content")))
        self.assertTrue(cart_content.is_displayed(), "Cart popup is not displayed")

        items = cart_content.find_elements(By.CSS_SELECTOR, "li.single-shopping-cart")
        self.assertTrue(len(items) > 0, "No items found in the cart popup")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()