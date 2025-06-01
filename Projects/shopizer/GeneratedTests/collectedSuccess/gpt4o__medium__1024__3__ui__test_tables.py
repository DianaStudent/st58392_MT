import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Check the presence and visibility of the 'Home' link
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")

        # Check the presence and visibility of the 'Tables' link
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

        # Check the presence and visibility of the 'Chairs' link
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Check the presence and visibility of the 'Login' button
        account_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        self.assertTrue(account_button.is_displayed(), "Account button is not visible")

        # Click 'Login' to test UI interaction
        account_button.click()
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_displayed(), "Login link did not appear after clicking account button")

        # Click 'Accept cookies' button
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")
        
        # Interact with 'Accept cookies' and verify no errors
        accept_cookies_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()