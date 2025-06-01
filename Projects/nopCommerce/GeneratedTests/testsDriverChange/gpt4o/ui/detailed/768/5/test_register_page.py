import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header visibility
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Verify footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Verify form section visibility
        registration_page = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "registration-page")))
        if not registration_page.is_displayed():
            self.fail("Registration page is not visible")

        # Verify form inputs visibility
        try:
            firstname = driver.find_element(By.ID, "FirstName")
            lastname = driver.find_element(By.ID, "LastName")
            email = driver.find_element(By.ID, "Email")
            password = driver.find_element(By.ID, "Password")
            confirmpassword = driver.find_element(By.ID, "ConfirmPassword")
        except Exception:
            self.fail("One or more required form fields are missing")

        form_inputs = [firstname, lastname, email, password, confirmpassword]
        for elem in form_inputs:
            if not elem.is_displayed():
                self.fail(f"{elem.get_attribute('name')} input is not visible")

        # Verify register button visibility and interaction
        register_button = driver.find_element(By.ID, "register-button")
        if not register_button.is_displayed():
            self.fail("Register button is not visible")

        # Click register button and check UI reaction
        register_button.click()

        # Expect form submission error messages due to empty fields
        validation_errors = driver.find_elements(By.CLASS_NAME, "field-validation-error")
        if not validation_errors:
            self.fail("Expected validation errors, but none were found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()