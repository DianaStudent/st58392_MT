import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver

        # Wait until 'CookieConsent' is visible and click 'Accept'
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "CookieConsent"))
            )
            accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie consent elements are missing: {str(e)}")

        # Check main header is visible
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header-area"))
            )
        except Exception as e:
            self.fail(f"Header area is missing: {str(e)}")

        # Check main navigation is visible
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "main-menu"))
            )
        except Exception as e:
            self.fail(f"Main menu is missing: {str(e)}")

        # Check footer is present
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer-area"))
            )
        except Exception as e:
            self.fail(f"Footer area is missing: {str(e)}")

        # Interact with the account setting button
        try:
            account_setting_button = driver.find_element(By.CLASS_NAME, "account-setting-active")
            self.assertTrue(account_setting_button.is_displayed(), "Account setting button is not visible")
            account_setting_button.click()
        except Exception as e:
            self.fail(f"Account setting elements are missing: {str(e)}")

        # Check login link is visible inside account dropdown
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
        except Exception as e:
            self.fail(f"Login link is missing in account dropdown: {str(e)}")

        # Check product buttons visibility
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@title='Add to cart']"))
            )
        except Exception as e:
            self.fail(f"Product buttons are missing: {str(e)}")

if __name__ == "__main__":
    unittest.main()