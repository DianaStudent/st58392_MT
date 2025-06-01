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
            cookie_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]")))
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Hover over the second product
        second_product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]")))
        actions = ActionChains(driver)
        actions.move_to_element(second_product).perform()

        # Click the "Add to cart" button
        add_to_cart_button2 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//button[@title='Add to cart']")))
        add_to_cart_button2.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible
        cart_popup = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content")))

        # Check if the cart popup is visible
        if not cart_popup.is_displayed():
            self.fail("Cart popup is not visible")

        # Click "View Cart" button inside the popup
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        cart_table = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-table-content")))
        if not cart_table:
            self.fail("Cart table not found")

        # Find product name elements
        product_name_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//td[@class='product-name']/a")))

        # Extract product names
        product_names = [element.text for element in product_name_elements]

        # Assert that expected product names are present
        if not product_names:
            self.fail("No product names found in the cart")
        self.assertIn("Chair", product_names)
        self.assertIn("Olive Table", product_names)

if __name__ == "__main__":
    unittest.main()