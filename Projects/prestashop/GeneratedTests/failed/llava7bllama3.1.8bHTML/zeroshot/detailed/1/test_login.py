from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_login(self):
        # Open the homepage
        self.driver.get("http://localhost:8080/en/")

        # Click the login link from the top navigation
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-name='login']"))
        ).click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )

        # Fill in the email and password fields using test credentials provided
        self.driver.find_element_by_name("email").send_keys("test@user.com")
        self.driver.find_element_by_name("password").send_keys("test@user1")

        # Click the submit button
        self.driver.find_element_by_id("submit").click()

        # Wait for the redirect after login
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@data-name='sign out']"))
        )

        # Confirm that login was successful by checking that:
        # - The "Sign out" button is present in the top navigation
        sign_out_button = self.driver.find_element_by_xpath("//a[@data-name='sign out']")
        self.assertIsNotNone(sign_out_button)

        # - The username (e.g. "test user") is also visible in the top navigation.
        username_text = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='username']"))
        )
        self.assertIsNotNone(username_text)
        self.assertNotEqual("", username_text.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()