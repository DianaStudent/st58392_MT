import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        return f"test_{random_suffix}@user.com"

    def test_registration(self):
        driver = self.driver

        # Open home page and click 'Sign in'
        sign_in_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        sign_in_link.click()

        # Click 'No account? Create one here' link on the login page
        create_account_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()

        # Fill registration form
        gender_mr = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='field-id_gender-1']")))
        gender_mr.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        firstname.send_keys("Test")

        lastname = driver.find_element(By.ID, "field-lastname")
        lastname.send_keys("User")

        email = driver.find_element(By.ID, "field-email")
        email.send_keys(self.generate_email())

        password = driver.find_element(By.ID, "field-password")
        password.send_keys("test@user1")

        birthday = driver.find_element(By.ID, "field-birthday")
        birthday.send_keys("01/01/1990")

        # Checkboxes
        psgdpr_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
        psgdpr_checkbox.click()

        customer_privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
        customer_privacy_checkbox.click()

        # Submit the form
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()

        # Confirm success by checking the presence of "Sign out"
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        sign_out = driver.find_element(By.LINK_TEXT, "Sign out")

        if not sign_out or sign_out.text.strip() == "":
            self.fail("Sign out link is not present, registration may have failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()