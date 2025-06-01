from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver

        # Step 1: Open home page — already done in setUp

        # Step 2: Click on the login link in the top menu
        try:
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
            )
            sign_in_link.click()
        except:
            self.fail("Sign in link is not available on home page.")

        # Step 3: Wait for the login page to load
        try:
            login_header = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[text()='Log in to your account']"))
            )
        except:
            self.fail("Login page did not load.")

        # Step 4: Fill in email and password
        try:
            email_field = driver.find_element(By.ID, "field-email")
            password_field = driver.find_element(By.ID, "field-password")
            email_field.send_keys("test@user.com")
            password_field.send_keys("test@user1")
        except:
            self.fail("Email or password field is missing.")

        # Step 5: Submit the login form
        try:
            submit_button = driver.find_element(By.ID, "submit-login")
            submit_button.click()
        except:
            self.fail("Submit button is not found.")

        # Step 6: Verify that login was successful by checking for "Sign out"
        try:
            sign_out_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
            assert sign_out_link.is_displayed(), "Sign out link should be displayed."
        except:
            self.fail("Login failed or 'Sign out' link is not visible.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()