from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Step 1: Open the homepage.
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//body/")))
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='register-link']/span")))

        # Step 2: Click on the "Register".
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//button[@class='button-1 register-link']"))
        )
        register_button.click()

        # Step 3: Wait for the registration page to load.
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//body/")))
        self.wait.until(EC.element_located((By.XPATH, "//div[@class='master-wrapper-page']")))
        self.wait.until(EC.element_located((By.XPATH, "//div[@class='master-wrapper-content']")))

        # Step 4: Fill all the fields.
        gender_select = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//label[@for='gender-male']"))
        )
        select_genders = Select(gender_select)
        select_genders.select_by_value("M")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='FirstName']")))
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[@id='FirstName']"))
        )
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='LastName']")))
        last_name_input.send_keys("User")
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[@id='Email']")))
        email_input.send_keys("test@example.com")

        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ConfirmPassword']")))
        confirm_password_input = WebDriverWait(self.driver, 20).until(
            EC.element_located((By.XPATH, "//input[@id='ConfirmPassword']")))
        confirm_password_input.send_keys("test11")

        # Step 5: Submit the registration form.
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='button-1 register-continue-button']"))
        )
        register_button.click()

        # Step 6: Verify that a message like "Your registration completed" is shown after successful registration.
        result_message = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='result']/span")))
        self.assertTrue("Your registration completed" in result_message)

if __name__ == "__main__":
    unittest.main()