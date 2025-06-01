import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_login(self):
        # Click login link from top navigation
        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign in"))
        )
        login_link.click()

        # Fill in email and password fields
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.send_keys("test@user.com")

        password_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_field.send_keys("test@user1")

        # Click submit button
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "submit"))
        )
        submit_button.click()

        # Wait for redirect after login
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
        )

        # Confirm that login was successful
        self.assertIn("Sign out", self.driver.page_source)
        username = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@data-name='username']"))
        )
        self.assertEqual(username.text.strip(), "test user")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()