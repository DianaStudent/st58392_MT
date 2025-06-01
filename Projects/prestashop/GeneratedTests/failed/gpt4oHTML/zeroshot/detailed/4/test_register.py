from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterUserTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"

    def generate_random_email(self):
        return "test_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@user.com"

    def test_register_user(self):
        driver = self.driver
        driver.get(self.base_url)

        # Navigate to Login Page
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='_desktop_user_info']//a[contains(.,'Sign in')]"))
        )
        login_link.click()

        # Click on Register Link
        register_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'No account? Create one here')]"))
        )
        register_link.click()

        # Fill in Registration Form
        gender_mr = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='field-id_gender-1']"))
        )
        gender_mr.click()

        first_name_field = driver.find_element(By.XPATH, "//input[@id='field-firstname']")
        first_name_field.send_keys("Test")

        last_name_field = driver.find_element(By.XPATH, "//input[@id='field-lastname']")
        last_name_field.send_keys("User")

        email_field = driver.find_element(By.XPATH, "//input[@id='field-email']")
        email_field.send_keys(self.generate_random_email())

        password_field = driver.find_element(By.XPATH, "//input[@id='field-password']")
        password_field.send_keys("test@user1")

        birthday_field = driver.find_element(By.XPATH, "//input[@id='field-birthday']")
        birthday_field.send_keys("01/01/2000")

        # Tick checkboxes for privacy, terms, and newsletter
        terms_checkbox = driver.find_element(By.XPATH, "//input[@name='psgdpr']")
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.XPATH, "//input[@name='customer_privacy']")
        privacy_checkbox.click()

        newsletter_checkbox = driver.find_element(By.XPATH, "//input[@name='newsletter']")
        newsletter_checkbox.click()
        
        # Submit Registration Form
        submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        submit_button.click()

        # Confirm registration/login successful
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='logout hidden-sm-down' and contains(text(), 'Sign out')]"))
        )

        user_info_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='account']/span[contains(text(), 'Test User')]"))
        )
        
        self.assertTrue(user_info_element.is_displayed(), "The user info is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()