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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Cookies accept button not found.")

        # Hover over the first product to reveal the "Add to cart" button
        try:
            product = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']"))
            )
            ActionChains(driver).move_to_element(product).perform()
        except:
            self.fail("Product element not found for hover action.")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = product.find_element(By.XPATH, ".//button[@title='Add to cart']")
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found.")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found.")

        # Confirm the popup contains at least one item
        try:
            cart_items = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".single-shopping-cart"))
            )
            self.assertIsNotNone(cart_items, "Cart popup does not contain any items.")
        except:
            self.fail("Cart popup did not open or contain items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()