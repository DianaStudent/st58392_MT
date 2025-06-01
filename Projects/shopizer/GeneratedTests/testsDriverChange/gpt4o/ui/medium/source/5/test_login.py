from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizerUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")  # Simulate steps to reach the page, adjust as needed
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify navigation links presence
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".main-menu a")))
            self.assertTrue(len(nav_links) > 0, "Navigation links are not present")
        except Exception as e:
            self.fail(f"Failed to find navigation links: {str(e)}")

        # Check presence of login fields
        try:
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            self.assertTrue(username_input.is_displayed() and password_input.is_displayed(),
                            "Login fields are not visible")
        except Exception as e:
            self.fail(f"Failed to find login fields: {str(e)}")

        # Check presence of login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        except Exception as e:
            self.fail(f"Failed to find login button: {str(e)}")

        # Check and interact with 'Accept Cookies' button
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
            self.assertTrue(accept_cookies_button.is_displayed(), "Accept Cookies button is not functional")
        except Exception as e:
            self.fail(f"Failed to interact with 'Accept Cookies' button: {str(e)}")

        # Verify that the logo is present
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")
        except Exception as e:
            self.fail(f"Failed to find Logo: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()