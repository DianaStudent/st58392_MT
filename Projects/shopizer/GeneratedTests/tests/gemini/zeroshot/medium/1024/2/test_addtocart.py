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

        # Accept cookies if present
        try:
            cookie_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except:
            pass

        # Hover over the first product image to reveal the "Add to cart" button
        product_image = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//a/img")))
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")))

        actions = ActionChains(driver)
        actions.move_to_element(product_image).perform()

        # Click the "Add to cart" button
        wait.until(EC.element_to_be_clickable(add_to_cart_button)).click()

        # Open the cart popup by clicking the cart icon
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        try:
            cart_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".shopping-cart-content.active ul li.single-shopping-cart")))
            self.assertTrue(len(cart_items) > 0, "No items found in the cart popup.")
        except:
            self.fail("Could not find any cart items in the popup.")

if __name__ == "__main__":
    unittest.main()