import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Open the homepage.
        self.driver.get(html_data["home_before_register"])

        # Click the "Register".
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='register-next-step-button']")))
        register_button.click()

        # Wait for the registration page to load.
        self.driver.get(html_data["register_page"])

        # Fill all the fields.
        gender_male = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@value='male']")))
        gender_female = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Female')]"))).click()
        
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "last-name")))
        last_name_input.send_keys("User")

        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys("testuser" + str(len(str(1))) + "@example.com")

        company_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "company-name")))
        company_input.send_keys("TestCorp")

        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))
        password_input.send_keys("test11")

        confirm_password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "confirm-password")))
        confirm_password_input.send_keys("test11")

        # Submit the registration form.
        register_button.submit()

        # Verify that a message like "Your registration completed" is shown after successful registration.
        result_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
        self.assertTrue(result_message.text.startswith("Your registration completed"))

if __name__ == '__main__':
    unittest.main()