from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def test_ui_elements_present_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are missing.")

        # Verify buttons and their visibility
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Add to cart']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[normalize-space()='Subscribe']")))
        except:
            self.fail("Buttons for 'Accept Cookies', 'Add to cart', or 'Subscribe' are missing.")

        # Verify inputs
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']")))
        except:
            self.fail("Subscribe input field is missing.")

        # Interact with elements
        try:
            accept_cookies_button.click()

            add_to_cart_button.click()
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
            cart_count = cart_icon.find_element(By.CLASS_NAME, "count-style").text
            self.assertEqual(cart_count, "1", "Cart count did not increase after adding item to cart.")
        except:
            self.fail("Interactions with 'Accept Cookies' or 'Add to cart' failed.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()