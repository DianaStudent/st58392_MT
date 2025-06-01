import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://localhost:8080/en/"
        self.driver.get(self.base_url)

    def test_login(self):
        wait = WebDriverWait(self.driver, 20)

        # Click on the 'Sign in' link
        sign_in_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Wait for the login page to load
        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))

        # Fill in the email and password fields
        email_field.send_keys("test@user.com")
        password_field = self.driver.find_element(By.ID, "field-password")
        password_field.send_keys("test@user1")

        # Submit the login form
        submit_button = self.driver.find_element(By.ID, "submit-login")
        submit_button.click()

        # Verify successful login by checking the presence of "Sign out"
        try:
            sign_out_element = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
            self.assertTrue(sign_out_element.is_displayed())
        except Exception as e:
            self.fail("Login failed: 'Sign out' not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()