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
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080")  # Set this to the actual URL of the test environment
    
    def tearDown(self):
        self.driver.quit()
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Hover over the first product image to reveal the "Add to cart" button
        product_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//img")))
        self.assertIsNotNone(product_image, "The product image is not found or not visible.")

        actions = ActionChains(driver)
        actions.move_to_element(product_image).perform()

        # Click on "Add to cart" button
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']")))
        self.assertIsNotNone(add_to_cart_btn, "The 'Add to cart' button is not found or not clickable.")
        add_to_cart_btn.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.same-style.cart-wrap .icon-cart")))
        self.assertIsNotNone(cart_icon, "The cart icon button is not found or not clickable.")
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        cart_items = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.shopping-cart-content.active ul")))
        self.assertIsNotNone(cart_items, "The cart popup is not displayed or no items are listed.")
        
        listed_items = cart_items.find_elements(By.XPATH, "./li[@class='single-shopping-cart']")
        self.assertGreater(len(listed_items), 0, "The cart popup does not contain any listed items.")

if __name__ == "__main__":
    unittest.main()