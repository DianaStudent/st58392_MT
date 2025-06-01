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
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies
            cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookies_button.click()
            
            # Hover over the first product to reveal the "Add to cart" button
            product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            add_to_cart_button = product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
            actions = ActionChains(driver)
            actions.move_to_element(product).perform()
            
            # Click "Add to cart"
            add_to_cart_button.click()

            # Click the cart icon to open the cart
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_button.click()

            # Check if cart popup contains at least one item
            cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".single-shopping-cart")))
            self.assertGreater(len(cart_items), 0, "Cart should have at least one item.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()