from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        try:
            accept_cookies = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies.click()
        except Exception as e:
            self.fail("Accept cookies button not found. Exception: " + str(e))

        try:
            # Locate the first product and hover over it
            product_element = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2'][1]"))
            )
            ActionChains(driver).move_to_element(product_element).perform()

            # Click the "Add to Cart" button
            add_to_cart_button = product_element.find_element(By.XPATH, ".//button[@title='Add to cart']")
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart process failed. Exception: " + str(e))

        try:
            # Open the cart popup by clicking the cart icon
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            # Verify that the shopping cart contains at least one item
            cart_content = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
            )
            items = cart_content.find_elements(By.CLASS_NAME, "single-shopping-cart")
            self.assertGreater(len(items), 0, "Cart should contain at least one item.")
        except Exception as e:
            self.fail("Cart validation failed. Exception: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()