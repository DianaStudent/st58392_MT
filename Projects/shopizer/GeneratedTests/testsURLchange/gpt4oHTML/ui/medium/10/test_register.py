import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Confirm the presence of navigation links
        navigation_links = ["Home", "Tables", "Chairs"]
        for link_text in navigation_links:
            link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"{link_text} link is not visible")

        # Confirm the presence of login and register links in the account dropdown menu
        account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        login_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Interact with the cookie consent button and verify UI update
        cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookie_button.click()
        # Checking if the cookie consent disappears after clicking
        self.wait.until(EC.invisibility_of_element((By.CLASS_NAME, "CookieConsent")))

        # Check presence of footer section with essential links
        footer_links = ["Contact", "Login", "Register"]
        for link_text in footer_links:
            link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"{link_text} link in footer is not visible")

        # Verify that clicking login doesn't cause errors in the UI
        login_link.click()
        self.assertTrue(driver.current_url.endswith("/login"), "Failed to navigate to Login page properly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()