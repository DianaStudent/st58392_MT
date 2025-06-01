import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_components_on_registration_page(self):
        driver = self.driver

        # Wait and check for the header
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible on the registration page.")
        
        # Wait and check for the form fields
        field_ids = ["FirstName", "LastName", "Email", "Password", "ConfirmPassword"]
        
        for field_id in field_ids:
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Form field with id '{field_id}' is not present on the registration page.")

        # Wait and check for gender radio buttons
        try:
            gender_div = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "gender")))
            self.assertTrue(gender_div)
        except:
            self.fail("Gender radio buttons are not visible on the registration page.")

        # Check for the register button
        try:
            register_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "register-button")))
            self.assertTrue(register_button.is_displayed())
        except:
            self.fail("Register button is not visible on the registration page.")
        
        # Check for the header menu presence
        try:
            header_menu = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
            self.assertTrue(header_menu)
        except:
            self.fail("Header menu is not present on the registration page.")
        
        # Check for the footer presence
        try:
            footer = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(footer)
        except:
            self.fail("Footer is not present on the registration page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()