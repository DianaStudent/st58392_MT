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
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']")))
        if not product_element:
            self.fail("Product element not found")

        hover = ActionChains(driver).move_to_element(product_element)
        hover.perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")))
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Hover over the second product to reveal the "Add to cart" button
        product_element2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']")))
        if not product_element2:
            self.fail("Product element not found")

        hover2 = ActionChains(driver).move_to_element(product_element2)
        hover2.perform()

        # Click the "Add to cart" button
        add_to_cart_button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//button[@title='Add to cart']")))
        if not add_to_cart_button2:
            self.fail("Add to cart button not found")
        add_to_cart_button2.click()

        # Open the cart popup
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        if not cart_icon:
            self.fail("Cart icon not found")
        cart_icon.click()

        # Verify that the cart popup contains at least one item
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='shopping-cart-content active']//li[@class='single-shopping-cart']")))
        except:
            self.fail("No items found in the cart popup")

if __name__ == "__main__":
    unittest.main()