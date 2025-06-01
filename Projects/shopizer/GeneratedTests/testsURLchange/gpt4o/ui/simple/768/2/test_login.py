import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
    
    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify header logo is present and visible
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
            self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")

            # Verify Home link is present and visible
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            # Verify Tables link is present and visible
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")

            # Verify Chairs link is present and visible
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

            # Verify login form elements
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            self.assertTrue(username_input.is_displayed(), "Username input is not visible")

            password_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "user-password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.button-box button")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Verify Accept Cookies button
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept Cookies button is not visible")

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()