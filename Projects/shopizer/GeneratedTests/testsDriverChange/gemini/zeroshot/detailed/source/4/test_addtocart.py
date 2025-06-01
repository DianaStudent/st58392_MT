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

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(first_product_locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(add_to_cart_button_locator)
        )
        add_to_cart_button.click()

        # Hover over the second product
        second_product_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]")
        second_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(second_product_locator)
        )
        actions = ActionChains(driver)
        actions.move_to_element(second_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button_locator = (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//button[@title='Add to cart']")
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(add_to_cart_button_locator)
        )
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon_locator = (By.CLASS_NAME, "icon-cart")
        cart_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(cart_icon_locator)
        )
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup_locator = (By.CLASS_NAME, "shopping-cart-content.active")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(cart_popup_locator)
        )

        # Click "View Cart" button inside the popup
        view_cart_button_locator = (By.XPATH, "//div[@class='shopping-cart-btn btn-hover text-center']/a[@href='/cart']")
        view_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(view_cart_button_locator)
        )
        view_cart_button.click()

        # Verify that the product appears in the cart list on the cart page
        product_name_locator = (By.XPATH, "//td[@class='product-name']/a")
        product_names = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located(product_name_locator)
        )

        if not product_names:
            self.fail("No products found in the cart.")

        product_names_text = [product.text for product in product_names]

        if not product_names_text:
            self.fail("Product names are empty.")

        expected_product_names = ["Chair", "Olive Table"]
        for expected_name in expected_product_names:
            if expected_name not in product_names_text:
                self.fail(f"Expected product '{expected_name}' not found in cart.")

if __name__ == "__main__":
    unittest.main()