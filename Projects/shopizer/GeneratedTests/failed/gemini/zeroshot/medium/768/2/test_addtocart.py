from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the product image to reveal the "Add to cart" button
        product_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]"))
        )
        if not product_element:
            self.fail("Product element not found.")

        product_image = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//a[@href='/product/olive-table']/img"))
        )
        if not product_image:
            self.fail("Product image not found.")

        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )
        if not cart_icon:
            self.fail("Cart icon not found.")
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='shopping-cart-content active']//li[@class='single-shopping-cart']"))
            )
            cart_items = driver.find_elements(By.XPATH, "//div[@class='shopping-cart-content active']//li[@class='single-shopping-cart']")
            self.assertTrue(len(cart_items) > 0, "No products found in the cart popup.")
        except:
            self.fail("Cart items not found in the popup.")


if __name__ == "__main__":
    unittest.main()