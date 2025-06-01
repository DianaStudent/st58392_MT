import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UiProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.driver.maximize_window()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header navigation links
            header_nav_links = ["Home", "Tables", "Chairs"]
            for link_text in header_nav_links:
                header_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertIsNotNone(header_link, f"{link_text} link is not visible")

            # Check Cookie Consent button
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertIsNotNone(accept_cookies_button, "Accept cookies button is not visible")

            # Check Login and Register links in header
            account_setting_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_setting_button.click()
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertIsNotNone(login_link, "Login link is not visible")
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertIsNotNone(register_link, "Register link is not visible")

            # Check footer links
            footer_links = ["Contact", "Login", "Register"]
            for link_text in footer_links:
                footer_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
                self.assertIsNotNone(footer_link, f"Footer link {link_text} is not visible")
            
            # Check subscription form
            subscription_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 input.email")))
            self.assertIsNotNone(subscription_input, "Subscription email input is not visible")
            subscription_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 .button")))
            self.assertIsNotNone(subscription_button, "Subscription button is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()