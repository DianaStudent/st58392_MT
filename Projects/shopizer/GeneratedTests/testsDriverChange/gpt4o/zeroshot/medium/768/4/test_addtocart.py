import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Cookie accept button not found or not clickable.")

        # Hover over product image to reveal "Add to cart" button
        try:
            product_image = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2 .product-img img")))
            ActionChains(driver).move_to_element(product_image).perform()

            add_to_cart_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Product image or 'Add to cart' button not interactable.")

        # Click on the cart icon to open the cart popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_icon.click()

            # Wait for the cart popup to open and check for items
            cart_items = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".single-shopping-cart")))
            if not cart_items:
                self.fail("Cart popup opened, but no items listed.")
        except:
            self.fail("Cart icon not clickable or cart popup did not contain items.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()