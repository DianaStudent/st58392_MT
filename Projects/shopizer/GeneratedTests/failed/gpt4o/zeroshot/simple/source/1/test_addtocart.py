from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies if present
        try:
            accept_cookies_btn = self.wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_btn.click()
        except:
            self.fail("Cookies acceptance button not clickable")

        # Hover over the first product to reveal "Add to cart" button
        product_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='product-wrap-2']//img"))
        )
        ActionChains(driver).move_to_element(product_element).perform()
        
        # Click "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Open cart popup by clicking the cart icon
        cart_icon = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()

        # Confirm success by checking that the popup contains at least one item
        cart_popup_item = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//ul/li[@class='single-shopping-cart']"))
        )
        self.assertTrue(cart_popup_item, "Cart popup does not contain items")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()