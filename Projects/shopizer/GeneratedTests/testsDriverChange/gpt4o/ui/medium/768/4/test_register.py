import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestKeyUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Verify header links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Verify login/register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            # Verify form inputs
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))

            # Verify language selector
            language_selector = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))

            # Verify buttons
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

            # Interact with elements
            accept_cookies_button.click()

            # Verify interaction
            if not accept_cookies_button.is_displayed():
                self.fail("Accept cookies button should not be visible after clicking.")

        except Exception as e:
            self.fail(f"Test failed: {e}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()