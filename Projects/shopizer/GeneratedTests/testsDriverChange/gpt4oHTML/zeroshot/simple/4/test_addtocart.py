import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_add_to_cart_and_check_popup(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception as e:
            self.fail(f"Cookie acceptance button not found or clickable: {str(e)}")

        # Hover over the first product
        try:
            product_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
            ActionChains(driver).move_to_element(product_element).perform()
        except Exception as e:
            self.fail(f"First product element not found or not hoverable: {str(e)}")

        # Click the "Add to cart" button
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"'Add to cart' button not found or not clickable: {str(e)}")

        # Click on the cart icon to open the popup
        try:
            cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart i.pe-7s-shopbag")))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon not found or not clickable: {str(e)}")

        # Confirm the popup contains at least one item
        try:
            popup_active = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active .single-shopping-cart")))
            self.assertTrue(popup_active.is_displayed(), "The cart popup does not contain any items")
        except Exception as e:
            self.fail(f"Cart popup with items not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()