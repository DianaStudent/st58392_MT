import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/register")

    def test_registration_page(self):
        # Check header is present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        header = self.driver.find_element(By.TAG_NAME, "h1")
        self.assertIsNotNone(header)
        self.assertEqual(header.text, "Registration")

        # Check form fields are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field = self.driver.find_element(By.NAME, "username")
        self.assertIsNotNone(username_field)

        email_field = self.driver.find_element(By.NAME, "email")
        self.assertIsNotNone(email_field)

        password_field = self.driver.find_element(By.NAME, "password")
        self.assertIsNotNone(password_field)

        confirm_password_field = self.driver.find_element(By.NAME, "confirm_password")
        self.assertIsNotNone(confirm_password_field)

        # Check buttons are present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.assertIsNotNone(submit_button)

        back_button = self.driver.find_element(By.LINK_TEXT, "Back")
        self.assertIsNotNone(back_button)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()