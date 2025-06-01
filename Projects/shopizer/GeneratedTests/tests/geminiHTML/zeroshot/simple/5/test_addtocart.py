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

        # Accept cookies if the consent form is present
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Find the first product element
        product_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
        )

        if not product_element:
            self.fail("Product element not found.")

        # Hover over the product to reveal the "Add to cart" button
        action = ActionChains(driver)
        action.move_to_element(product_element).perform()

        # Find the "Add to cart" button within the product
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )

        if not add_to_cart_button:
            self.fail("Add to cart button not found.")

        # Click the "Add to cart" button
        add_to_cart_button.click()

        # Find the cart icon
        cart_icon = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
        )

        if not cart_icon:
            self.fail("Cart icon not found.")

        # Click the cart icon to open the cart popup
        cart_icon.click()

        # Wait for the cart popup to appear and check if it contains at least one item
        try:
            WebDriverWait(driver, 20).until(
                lambda driver: driver.find_element(By.CSS_SELECTOR, ".shopping-cart-content ul li")
            )
        except:
            self.fail("Cart popup did not open or is empty.")

        # Verify that the cart popup is active
        cart_popup = driver.find_element(By.CLASS_NAME, "shopping-cart-content")
        self.assertTrue("active" in cart_popup.get_attribute("class"), "Cart popup is not active")


if __name__ == "__main__":
    unittest.main()