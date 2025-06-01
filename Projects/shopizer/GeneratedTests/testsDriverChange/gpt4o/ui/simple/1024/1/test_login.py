import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
            self.assertIsNotNone(header, "Header is missing or not visible")

            # Verify logo
            logo = header.find_element(By.TAG_NAME, 'img')
            self.assertIsNotNone(logo, "Logo is missing or not visible")

            # Verify menu links
            menu = header.find_element(By.CLASS_NAME, 'main-menu')
            self.assertIsNotNone(menu.find_element(By.LINK_TEXT, "Home"), "Home link is missing or not visible")
            self.assertIsNotNone(menu.find_element(By.LINK_TEXT, "Tables"), "Tables link is missing or not visible")
            self.assertIsNotNone(menu.find_element(By.LINK_TEXT, "Chairs"), "Chairs link is missing or not visible")

            # Verify login button
            account_setting = header.find_element(By.CLASS_NAME, 'account-setting')
            self.assertIsNotNone(account_setting.find_element(By.LINK_TEXT, "Login"), "Login link is missing or not visible")

            # Verify register button
            self.assertIsNotNone(account_setting.find_element(By.LINK_TEXT, "Register"), "Register link is missing or not visible")

        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

        # Check bottom-cookie consent
        try:
            consent = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'CookieConsent')))
            self.assertIsNotNone(consent, "Cookie consent is missing or not visible")
            accept_button = consent.find_element(By.ID, 'rcc-confirm-button')
            self.assertIsNotNone(accept_button, "Accept button is missing or not visible")

        except Exception as e:
            self.fail(f"Exception occurred: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()