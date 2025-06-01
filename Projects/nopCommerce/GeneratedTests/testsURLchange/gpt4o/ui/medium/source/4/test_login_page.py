import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check presence and visibility of header links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            my_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
        except Exception as e:
            self.fail(f"Header links not found or not visible: {e}")

        # Check presence and visibility of login form elements
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        except Exception as e:
            self.fail(f"Login form elements not found or not visible: {e}")

        # Interact with input and buttons
        email_input.send_keys("test@example.com")
        password_input.send_keys("password")

        # Click login button and verify no UI errors
        try:
            login_button.click()
            # For the purpose of this test, ensure no JavaScript alert or new error elements appear
            alert_present = driver.execute_script("return !!window.alert")
            self.assertFalse(alert_present, "Unexpected JavaScript alert present")
        except Exception as e:
            self.fail(f"Interaction with login button failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()