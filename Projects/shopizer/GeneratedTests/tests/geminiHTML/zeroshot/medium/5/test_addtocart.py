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
        wait = WebDriverWait(driver, 20)

        # Accept cookies if the consent banner is present
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product to reveal the "Add to cart" button
        product_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")
            )
        )
        if not product_element:
            self.fail("Product element not found.")

        # Hover over the product image
        product_image = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//a/img")
            )
        )
        if not product_image:
            self.fail("Product image not found.")

        actions = ActionChains(driver)
        actions.move_to_element(product_image).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")
            )
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found.")

        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='same-style cart-wrap d-none d-lg-block']/button[@class='icon-cart']")
            )
        )
        if not cart_icon:
            self.fail("Cart icon not found.")

        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        cart_items = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@class='shopping-cart-content active']/ul/li[@class='single-shopping-cart']")
            )
        )

        if not cart_items:
            self.fail("No items found in the cart popup.")

        self.assertTrue(len(cart_items) > 0, "No product in cart popup")


if __name__ == "__main__":
    unittest.main()