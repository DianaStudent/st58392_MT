import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence of navigation links and UI components
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")
        except Exception as e:
            self.fail(f"Navigation links not found: {str(e)}")

        # Check presence of login button and form
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.account-setting-active")))
            account_button.click()

            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")

            login_link.click()
            username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit'] > span")))

            self.assertTrue(username_input.is_displayed(), "Username input is not visible")
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")
        except Exception as e:
            self.fail(f"Login elements not found or could not interact: {str(e)}")

        # Interact and check for UI errors (basic interaction)
        username_input.send_keys("test@example.com")
        password_input.send_keys("password")
        login_button.click()

        # Confirm no UI errors (presence of a specific element after interaction)
        try:
            welcome_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb-content")))
            self.assertTrue(welcome_message.is_displayed(), "No welcome message or unexpected UI error after login attempt")
        except Exception as e:
            self.fail(f"UI error after login attempt: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()