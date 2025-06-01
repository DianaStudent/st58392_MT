from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ShopUIElementsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check buttons
            cookie_accept_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.icon-cart")))

            # Check footer elements
            footer_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.footer-area")))

            # Check form elements
            subscribe_email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form input[type='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form button.button")))

            # Check product page navigation
            login_page_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_page_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("One or more UI elements are missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()