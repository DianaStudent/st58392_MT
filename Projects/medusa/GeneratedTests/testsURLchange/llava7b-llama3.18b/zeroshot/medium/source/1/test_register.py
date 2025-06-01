import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_register_user(self):
        # Click the "Account" link
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Account']"))).click()

        # Click the "Join Us" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Join Us']"))).click()

        # Fill in all fields: first name, last name, email (generate it unique), password
        first_name_field = self.driver.find_element(By.XPATH, "//input[@name='first_name']")
        last_name_field = self.driver.find_element(By.XPATH, "//input[@name='last_name']")
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        password_field = self.driver.find_element(By.XPATH, "//input[@type='password']")

        first_name_field.send_keys("user")
        last_name_field.send_keys("test")
        # Generate a unique email
        import uuid
        email_id = str(uuid.uuid4()) + "@test.com"
        email_field.send_keys(email_id)
        password_field.send_keys("testuser")

        # Submit the registration form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='CONTINUE']"))).click()

        # Fill in all fields: first name, last name, email (generate it unique), password
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='first_name']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='last_name']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))

        first_name_field.send_keys("user")
        last_name_field.send_keys("test")
        # Generate a unique email
        email_id = str(uuid.uuid4()) + "@test.com"
        email_field.clear()
        email_field.send_keys(email_id)
        password_field.clear()
        password_field.send_keys("testuser")

        # Submit the registration form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='CONTINUE']"))).click()

        # Click the "ACCEPT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='accept-button']"))).click()

        # Verify registration success by checking presence of welcome message
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Welcome to Medusa Store!']")))

if __name__ == "__main__":
    unittest.main()