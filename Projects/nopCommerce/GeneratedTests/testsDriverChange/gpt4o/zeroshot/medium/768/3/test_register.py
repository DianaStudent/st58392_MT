import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the "Register"
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        if not register_link.text:
            self.fail("Register link is empty or not found")
        register_link.click()

        # Step 3: Wait for the registration page to load.
        wait.until(EC.presence_of_element_located((By.ID, "FirstName")))

        # Step 4: Fill all the fields.
        driver.find_element(By.ID, "gender-female").click()
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")
        
        # Dynamically generate an email
        email = f"testuser{int(time.time())}@test.com"
        driver.find_element(By.ID, "Email").send_keys(email)

        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # Step 5: Submit the registration form.
        register_button = driver.find_element(By.ID, "register-button")
        if not register_button.text:
            self.fail("Register button is empty or not found")
        register_button.click()

        # Step 6: Verify the success message.
        registration_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        message_text = registration_message.text
        if not message_text:
            self.fail("Registration completed message is empty or not found")
        
        self.assertTrue(re.search("Your registration completed", message_text), "Registration message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()