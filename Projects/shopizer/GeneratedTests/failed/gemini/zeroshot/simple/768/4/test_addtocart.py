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
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Hover over the first product "Olive Table"
        try:
            product = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']"))
            )
            ActionChains(driver).move_to_element(product).perform()
        except:
            self.fail("Could not find the product 'Olive Table'")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button for 'Olive Table'")

        # Hover over the second product "Chair"
        try:
            product = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']"))
            )
            ActionChains(driver).move_to_element(product).perform()
        except:
            self.fail("Could not find the product 'Chair'")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the 'Add to cart' button for 'Chair'")

        # Open the cart popup
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Could not find or click the cart icon")

        # Check if the cart popup contains at least one item
        try:
            cart_items = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".shopping-cart-content ul li.single-shopping-cart"))
            )
            self.assertTrue(len(cart_items) > 0, "Cart popup is empty")
        except:
            self.fail("Could not find cart items in the popup")

if __name__ == "__main__":
    unittest.main()