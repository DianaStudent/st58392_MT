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

        # Hover over the first product to reveal the "Add to cart" button
        try:
            product = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]"))
            )
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']"))
            )

            actions = ActionChains(driver)
            actions.move_to_element(product).perform()
            add_to_cart_button.click()

        except Exception as e:
            self.fail(f"Could not hover and click add to cart button: {e}")

        # Hover over the second product to reveal the "Add to cart" button
        try:
            product2 = wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]"))
            )
            add_to_cart_button2 = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//button[@title='Add to cart']"))
            )

            actions = ActionChains(driver)
            actions.move_to_element(product2).perform()
            add_to_cart_button2.click()

        except Exception as e:
            self.fail(f"Could not hover and click add to cart button: {e}")

        # Open the cart popup by clicking the cart icon
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Could not click cart icon: {e}")

        # Confirm success by checking that the popup contains at least one item
        try:
            cart_popup_content = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
            )
            cart_items = cart_popup_content.find_elements(By.CLASS_NAME, "single-shopping-cart")
            self.assertGreater(len(cart_items), 0, "Cart popup should contain at least one item")
        except Exception as e:
            self.fail(f"Could not verify cart popup content: {e}")

if __name__ == "__main__":
    unittest.main()