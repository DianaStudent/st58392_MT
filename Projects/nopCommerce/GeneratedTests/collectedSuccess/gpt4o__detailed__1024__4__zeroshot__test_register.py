import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open homepage and click "Register"
        try:
            register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        except Exception as e:
            self.fail(f"Register link not found: {str(e)}")
        
        register_link.click()

        # Step 3: Wait for the registration form to load
        try:
            gender_female_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        except Exception as e:
            self.fail(f"Registration form failed to load: {str(e)}")

        # Step 4: Select gender
        gender_female_radio.click()

        # Step 5: Fill required fields
        try:
            driver.find_element(By.ID, "FirstName").send_keys("Test")
            driver.find_element(By.ID, "LastName").send_keys("User")
            driver.find_element(By.ID, "Email").send_keys(f"testuser{int(time.time())}@example.com")
            driver.find_element(By.ID, "Company").send_keys("TestCorp")
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to fill required fields: {str(e)}")

        # Step 6: Submit the form
        try:
            register_button = driver.find_element(By.ID, "register-button")
        except Exception as e:
            self.fail(f"Register button not found: {str(e)}")

        register_button.click()

        # Step 7: Wait for confirmation
        try:
            confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.result")))
            self.assertIn("Your registration completed", confirmation_message.text)
        except Exception as e:
            self.fail(f"Registration confirmation failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()