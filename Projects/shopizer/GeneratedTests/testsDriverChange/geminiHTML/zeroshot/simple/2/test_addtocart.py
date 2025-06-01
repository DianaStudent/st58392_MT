import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find a product element (e.g., the Olive Table)
        try:
            product_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h3/a[text()='Olive Table']/ancestor::div[@class='product-content-2']/preceding-sibling::div[@class='product-img']"))
            )
        except:
            self.fail("Product element not found")

        # Hover over the product to reveal the "Add to cart" button
        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        # Find and click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//h3/a[text()='Olive Table']/ancestor::div[@class='product-content-2']/preceding-sibling::div[@class='product-img']//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Find and click the cart icon to open the cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found or not clickable")

        # Verify that the cart popup contains at least one item
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='shopping-cart-content active']/ul/li"))
            )
        except:
            self.fail("Cart popup does not contain any items")


if __name__ == "__main__":
    unittest.main()