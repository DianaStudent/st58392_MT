import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        
        # Step 1: Open the homepage
        self.assertIn("Your store name", driver.page_source)
        
        # Step 2: Click the "Register" link in the top navigation
        try:
            register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
            register_link.click()
        except:
            self.fail("Register link was not found or clicked.")

        # Step 3: Wait for the registration form to load
        self.wait.until(EC.presence_of_element_located((By.ID, "main")))

        # Step 4: Select the appropriate gender radio input
        try:
            female_radio = driver.find_element(By.ID, "gender-female")
            female_radio.click()
        except:
            self.fail("Female gender radio button was not found or clicked.")
        
        # Step 5: Fill in all required fields
        try:
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            dynamic_email = f"testuser{int(time.time())}@test.com"
            driver.find_element(By.ID, "Email").send_keys(dynamic_email)
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except:
            self.fail("One or more form fields were not found or filled.")

        # Step 6: Submit the registration form
        try:
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()
        except:
            self.fail("Register button was not found or clicked.")
        
        # Step 7: Wait for the response page or confirmation message to load
        success_message_locator = (By.CSS_SELECTOR, ".result")
        try:
            registration_success = self.wait.until(EC.presence_of_element_located(success_message_locator))
        except:
            self.fail("Registration success message was not found or loaded.")
        
        # Step 8: Verify registration success
        self.assertIn("Your registration completed", registration_success.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()