import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080")  # Replace with the actual URL
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        action_chains = ActionChains(driver)

        # Accept cookies if the cookie consent popup appears
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            pass  # Proceed if the cookies consent button is not found

        # Hover over product to reveal "Add to cart" button
        try:
            product = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-action-2']//button[contains(@title, 'Add to cart') and contains(@class, 'active')]")))
            action_chains.move_to_element(product).perform()
            add_to_cart_button = product.find_element(By.XPATH, "./i[contains(@class, 'fa-shopping-cart')]")
            add_to_cart_button.click()
        except:
            self.fail("Could not find the Add to cart button or hover action failed.")
        
        # Click on the cart icon button to open cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.header-right-wrap button.icon-cart")))
            cart_icon.click()
        except:
            self.fail("Could not find the cart icon button.")
        
        # Confirm that cart popup contains at least one item
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.shopping-cart-content.active ul li.single-shopping-cart")))
        except:
            self.fail("Cart popup does not have any items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()