import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPages(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):
        # Open the login page
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        try:
            # Verify navigation links are present
            self.assertIsNotNone(self.driver.find_element(By.XPATH, "//nav"))
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))

            # Verify form fields and buttons are present
            email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
            password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
            forgot_password_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Forgot your password?')]")
            login_button = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

        except Exception as e:
            # If any required element is missing, fail the test
            self.fail("Required elements are not present: " + str(e))

if __name__ == "__main__":
    unittest.main()