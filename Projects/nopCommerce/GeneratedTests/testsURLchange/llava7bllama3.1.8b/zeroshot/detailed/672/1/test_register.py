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
        self.driver.get("http://max/")

    def test_registration(self):
        # Click the "Register" link in the top navigation
        register_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Sign Up'))
        )
        register_link.click()

        # Select gender radio input based on provided data
        female_gender_radio = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@value='female']"))
        )
        female_gender_radio.click()

        # Fill in all required fields
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'firstname'))
        )
        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'lastname'))
        )
        email_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'email'))
        )
        company_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'company'))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        confirm_password_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'confirm_password'))
        )

        first_name_input.send_keys('Test')
        last_name_input.send_keys('User')
        email_input.send_keys('test' + str(123) + '@example.com') # dynamically generated
        company_input.send_keys('TestCorp')
        password_input.send_keys('test11')
        confirm_password_input.send_keys('test11')

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_button.click()

        # Wait for the response page or confirmation message to load
        result_text = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Your registration completed')]"))
        )

        # Verify that registration succeeded
        self.assertTrue(result_text.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()