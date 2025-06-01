import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Click the login link
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[span[text()='Sign in']]")))
        sign_in_link.click()
        
        # Step 2: On the login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()
        
        # Step 3: Fill in the fields
        gender = wait.until(EC.presence_of_element_located((By.XPATH, "//label[@for='field-id_gender-1']/span/input")))
        gender.click()

        firstname = driver.find_element(By.ID, "field-firstname")
        lastname = driver.find_element(By.ID, "field-lastname")
        email = driver.find_element(By.ID, "field-email")
        password = driver.find_element(By.ID, "field-password")
        birthday = driver.find_element(By.ID, "field-birthday")

        firstname.send_keys("Test")
        lastname.send_keys("User")
        
        # Generate dynamic email
        random_number = random.randint(100000, 999999)
        email.send_keys(f"test_{random_number}@user.com")
        
        password.send_keys("test@user1")
        birthday.send_keys("01/01/2000")
        
        # Tick checkboxes
        self.tick_checkbox(driver, "optin")
        self.tick_checkbox(driver, "psgdpr")
        self.tick_checkbox(driver, "newsletter")
        self.tick_checkbox(driver, "customer_privacy")
        
        # Step 4: Submit the registration form
        save_button = driver.find_element(By.XPATH, "//button[@type='submit' and text()='Save']")
        save_button.click()
        
        # Step 5: Confirm success
        try:
            user_info = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-info")))
            sign_out = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='logout' and contains(text(), 'Sign out')]")))
            account_name = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//a[@class='account']/span[contains(text(), 'Test User')]")))

            self.assertTrue(user_info is not None)
            self.assertTrue(sign_out is not None)
            self.assertTrue(account_name is not None)
        except Exception as e:
            self.fail("Registration process failed, Sign out button or username not found.")

    def tick_checkbox(self, driver, name):
        checkbox = driver.find_element(By.NAME, name)
        if not checkbox.is_selected():
            checkbox.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()