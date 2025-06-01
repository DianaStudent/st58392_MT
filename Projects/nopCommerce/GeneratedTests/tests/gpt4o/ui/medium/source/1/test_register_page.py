from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_registration_page_ui_elements(self):
        driver = self.driver

        try:
            # Wait for and verify main UI components are present and visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "page-body")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "FirstName")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "LastName")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email")))
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "register-button")))

            # Interact with inputs and buttons
            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("John")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("Doe")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys("john.doe@example.com")

            # Click the register button
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Verify no UI error after interaction
            WebDriverWait(driver, 20).until(
                EC.invisibility_of_element((By.ID, "dialog-notifications-error")))

        except TimeoutException as e:
            self.fail(f"Test failed due to TimeoutException: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()