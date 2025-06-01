from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Load the register page
        driver.get("http://max/register?returnUrl=%2F")

        # Check presence of header and footer
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))

        if not header or not footer:
            self.fail("Required header or footer element is missing")

        # Check form fields and labels are present and visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "FirstName"))), "First name field is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "LastName"))), "Last name field is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "Email"))), "Email field is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "Password"))), "Password field is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword"))), "Confirm password field is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "register-button"))), "Register button is missing")

        # Check gender radio buttons
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "gender-male"))), "Male radio button is missing")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "gender-female"))), "Female radio button is missing")

        # Click the Register button
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Confirm the UI reacts visually (e.g., validation messages appear)
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "field-validation-valid"))), "Validation message did not appear")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()