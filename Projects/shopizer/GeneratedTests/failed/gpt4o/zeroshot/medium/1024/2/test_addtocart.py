from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        ).click()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        action = ActionChains(driver)
        
        # Hover over the first product to reveal the "Add to cart" button
        product_img = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.product-img img")
        ))
        action.move_to_element(product_img).perform()

        # Click the "Add to cart" button for the first product
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.product-action-2 button[title='Add to cart']")
        ))
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.icon-cart")
        ))
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        cart_content = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.shopping-cart-content")
        ))
        product_list = cart_content.find_elements(By.CSS_SELECTOR, "li.single-shopping-cart")

        self.assertTrue(len(product_list) > 0, "No products found in the cart popup.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()