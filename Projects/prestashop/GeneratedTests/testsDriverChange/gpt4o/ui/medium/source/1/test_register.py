import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")

    def test_page_elements(self):
        driver = self.driver

        try:
            # Wait and check for main header
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "h1"))
            )
            
            # Check for navigation links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Sign in"))
            )

            # Check for form fields
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-firstname"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-lastname"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-email"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "field-password"))
            )

            # Check for buttons
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
            )
            
            # Interact with a button and check no error
            submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            submit_button.click()
            
            # Verify UI updates, no crash
            error_message = driver.find_elements(By.CLASS_NAME, "form-error-message")
            if error_message:
                self.fail("Form submission resulted in errors: {}".format(error_message))

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()