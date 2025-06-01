import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except:
            self.fail("Header is missing")

        # Check footer visibility
        try:
            footer = driver.find_element(By.ID, 'footer')
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Footer is missing")

        # Check navigation visibility
        try:
            navigation = driver.find_element(By.XPATH, "//nav[@class='header-nav']")
            self.assertTrue(navigation.is_displayed(), "Navigation is not visible")
        except:
            self.fail("Navigation is missing")

        # Check for email field
        try:
            email_field = driver.find_element(By.ID, 'field-email')
            self.assertTrue(email_field.is_displayed(), "Email field is not visible")
        except:
            self.fail("Email field is missing")

        # Check for password field
        try:
            password_field = driver.find_element(By.ID, 'field-password')
            self.assertTrue(password_field.is_displayed(), "Password field is not visible")
        except:
            self.fail("Password field is missing")

        # Check for submit button
        try:
            submit_button = driver.find_element(By.ID, 'submit-login')
            self.assertTrue(submit_button.is_displayed(), "Submit button is not visible")
        except:
            self.fail("Submit button is missing")

        # Check for forgot password link
        try:
            forgot_password = driver.find_element(By.LINK_TEXT, 'Forgot your password?')
            self.assertTrue(forgot_password.is_displayed(), "Forgot password link is not visible")
        except:
            self.fail("Forgot password link is missing")

        # Interact with elements
        email_field.send_keys('test@example.com')
        password_field.send_keys('password')
        submit_button.click()

        # Confirm that the UI reacts visually
        try:
            self.wait.until(EC.url_changes("http://localhost:8080/en/login"))
        except:
            self.fail("UI did not react as expected after submitting the form")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()