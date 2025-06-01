import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the login link in the top menu
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Wait for login page to load
        wait.until(EC.presence_of_element_located((By.ID, "login-form")))

        # Fill in the email and password fields
        email_field = driver.find_element(By.ID, "field-email")
        password_field = driver.find_element(By.ID, "field-password")
        email_field.send_keys("test@user.com")
        password_field.send_keys("test@user1")

        # Submit the login form
        login_button = driver.find_element(By.ID, "submit-login")
        login_button.click()

        # Verify that login was successful by checking for the presence of "Sign out"
        try:
            sign_out_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            assert "Sign out" in sign_out_element.text
        except Exception as e:
            self.fail(f"Login failed or element not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()