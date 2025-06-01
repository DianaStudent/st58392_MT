import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        # Wait for the page to load completely
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button#rcc-confirm-button"))
        ).click()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Hover over the product to reveal the "Add to cart" button
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-wrap-2")))
        add_to_cart_button = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-action-2 > button[title='Add to cart']"))
        )
        
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        
        ActionChains(driver).move_to_element(product).click(add_to_cart_button).perform()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.icon-cart"))
        )
        
        if not cart_icon:
            self.fail("Cart icon not found")
        
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        shopping_cart_content = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.shopping-cart-content ul"))
        )
        
        if not shopping_cart_content:
            self.fail("Shopping cart content not found")
        
        items = shopping_cart_content.find_elements(By.CSS_SELECTOR, "li.single-shopping-cart")
        self.assertGreater(len(items), 0, "No items found in the cart popup")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()