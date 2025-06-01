import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver
        wait = self.wait

        # Click the "Register" link in the top navigation
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the registration form to load
        wait.until(EC.presence_of_element_located((By.ID, "register-button")))

        # Select gender: Female
        gender_female = driver.find_element(By.ID, "gender-female")
        gender_female.click()

        # Fill in the required fields
        driver.find_element(By.ID, "FirstName").send_keys("Test")
        driver.find_element(By.ID, "LastName").send_keys("User")

        # Generate a unique email
        unique_email = f"testuser{int(time.time())}@example.com"
        driver.find_element(By.ID, "Email").send_keys(unique_email)

        driver.find_element(By.ID, "Company").send_keys("TestCorp")
        driver.find_element(By.ID, "Password").send_keys("test11")
        driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

        # Submit the form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Wait for the response page to load
        result_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))

        # Verify the registration completion message
        self.assertIn("Your registration completed", result_element.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()