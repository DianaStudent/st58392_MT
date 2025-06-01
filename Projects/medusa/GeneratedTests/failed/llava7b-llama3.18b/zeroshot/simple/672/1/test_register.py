from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_registration(self):
        # Fill all fields for registration
        self.driver.find_element(By.NAME, 'name').send_keys('user')
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        email_input.send_keys('test' + str(1234567890) + '@example.com')  # Generate a dynamic email

        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password_input.send_keys('testuser')

        # Confirm success by checking that the welcome message is present
        self.driver.find_element(By.NAME, 'confirm').click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[text()='Congratulations! Your account has been created.']"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=[__file__], exit=False)