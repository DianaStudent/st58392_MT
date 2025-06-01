import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UIAutomationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify presence of Navigation Links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Main navigation links are missing or not visible")

        # Verify accept cookies button and click it
        try:
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button is missing or not visible")

        # Verify that clicking login doesn't cause UI errors
        try:
            login_link.click()
            wait.until(EC.visibility_of_element_located((By.ID, "root"))) # Dummy check to see if page transitions
        except:
            self.fail("Clicking login link causes UI errors or doesn't transition")

        # Checking the subscribe form field and button
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button")))
            self.assertTrue(email_input.is_displayed() and subscribe_button.is_displayed(), "Subscribe form elements are missing or not visible")
        except:
            self.fail("Subscribe form elements are missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()