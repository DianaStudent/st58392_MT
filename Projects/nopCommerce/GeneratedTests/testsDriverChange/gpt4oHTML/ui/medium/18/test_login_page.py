import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui(self):
        driver = self.driver
        wait = self.wait

        # Check presence of main UI components
        try:
            # Check header links
            register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
            login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-login")))

            # Check if form elements are present
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))

            # Check if buttons are present
            login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.login-button")))

            # Interact with an element - Click on login button
            login_button.click()

            # Verify that the elements did not cause errors in the UI.
            error_notifications = driver.find_element(By.ID, "dialog-notifications-error")
            self.assertFalse(error_notifications.is_displayed(), "Error notifications should not be displayed!")
            
        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()