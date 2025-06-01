import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        
    def generate_random_email(self):
        return 'testuser' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + '@example.com'

    def test_register_user(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage and click the "Register" link
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link not found on homepage.")

        # Step 3: Wait for the registration form to load
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))
        except:
            self.fail("Registration form did not load.")

        # Step 4: Select the gender as Female
        try:
            female_radio = driver.find_element(By.ID, "gender-female")
            if not female_radio.is_selected():
                female_radio.click()
        except:
            self.fail("Gender radio button could not be found or selected.")

        # Step 5: Fill in the required fields
        try:
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            email = self.generate_random_email()
            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except:
            self.fail("Could not fill in registration fields.")

        # Step 6: Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button not found.")

        # Step 7: Wait for confirmation message
        try:
            confirmation_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result']")))
            self.assertTrue("Your registration completed" in confirmation_message.text)
        except:
            self.fail("Registration confirmation message not found or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()