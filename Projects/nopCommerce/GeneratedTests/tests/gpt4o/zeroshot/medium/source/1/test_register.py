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
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage and click "Register"
        register_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Register')]")))
        register_link.click()

        # 2. Wait for the registration page to load
        page_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Register')]")))
        self.assertTrue(page_title.is_displayed(), "Registration page did not load correctly.")

        # 3. Fill all the fields
        gender_female = driver.find_element(By.ID, "gender-female")
        gender_female.click()

        first_name = driver.find_element(By.ID, "FirstName")
        last_name = driver.find_element(By.ID, "LastName")
        email = driver.find_element(By.ID, "Email")
        company = driver.find_element(By.ID, "Company")
        password = driver.find_element(By.ID, "Password")
        confirm_password = driver.find_element(By.ID, "ConfirmPassword")

        # Generate a dynamic email
        email_value = f"testuser{int(time.time())}@example.com"

        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys(email_value)
        company.send_keys("TestCorp")
        password.send_keys("test11")
        confirm_password.send_keys("test11")

        # 4. Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # 5. Verify that a message like "Your registration completed" is shown
        registration_result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Your registration completed')]")))
        
        if not registration_result or not registration_result.is_displayed():
            self.fail("Registration was not successful or message not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()