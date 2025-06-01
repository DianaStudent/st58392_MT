import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080")  # Assuming this is the base URL of the website
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait
        
        # Locate the product element
        try:
            product = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-wrap-2']")))
        except Exception as e:
            self.fail(f"Product item not found: {str(e)}")

        # Hover over the product to reveal 'Add to cart'
        try:
            actions = ActionChains(driver)
            actions.move_to_element(product).perform()
        except Exception as e:
            self.fail(f"Unable to hover over product: {str(e)}")

        # Click the 'Add to cart' button
        try:
            add_to_cart_button = product.find_element(By.XPATH, ".//button[@title='Add to cart']")
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"'Add to cart' button not found: {str(e)}")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='icon-cart']")))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon not clickable: {str(e)}")

        # Confirm that the popup contains at least one item
        try:
            cart_items = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='shopping-cart-content active']//li[@class='single-shopping-cart']")))
            self.assertTrue(cart_items.is_displayed(), "Cart popup does not contain any items.")
        except Exception as e:
            self.fail(f"Cart popup items not found or not displayed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()