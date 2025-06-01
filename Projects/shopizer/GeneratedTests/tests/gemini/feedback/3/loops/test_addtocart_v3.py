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
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Hover over the second product
        second_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(second_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
        )
        add_to_cart_button2.click()

        # Click the cart icon to open the popup
        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()

        # Wait for the cart popup to become visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
        )

        # Click "View Cart" button
        view_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='shopping-cart-btn btn-hover text-center']/a[@href='/cart']"))
        )
        view_cart_button.click()

        # Verify that the product appears in the cart list
        try:
            product_in_cart = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='table-content table-responsive cart-table-content']//a[text()='Chair']"))
            )
            self.assertTrue(product_in_cart.text == 'Chair')
        except:
            self.fail("Product not found in cart")

if __name__ == "__main__":
    unittest.main()