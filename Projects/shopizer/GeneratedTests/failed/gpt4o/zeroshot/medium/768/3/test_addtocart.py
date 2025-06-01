from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Wait for the page to load
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-wrap-2")))

        # Hover over the first product to reveal the "Add to cart" button
        first_product = driver.find_element(By.CSS_SELECTOR, ".product-wrap-2")
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = driver.find_element(By.CSS_SELECTOR, ".icon-cart")
        cart_icon.click()

        # Wait for the cart popup to be visible and check if it contains at least one item
        cart_content = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content ul")))
        items = cart_content.find_elements(By.TAG_NAME, "li")
        
        # Verify that there is at least one product in the cart popup
        if not items:
            self.fail("No items found in the cart popup")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()