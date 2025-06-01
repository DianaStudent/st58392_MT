import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the main header and menu are visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header"))), "Header is not visible.")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu"))), "Top menu is not visible.")

        # Check the registration form is present
        register_form = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "registration-page")))
        self.assertIsNotNone(register_form, "Registration page is not found.")

        # Check form fields are visible
        fields_to_check = [
            (By.ID, "gender-male"),
            (By.ID, "gender-female"),
            (By.ID, "FirstName"),
            (By.ID, "LastName"),
            (By.ID, "Email"),
            (By.ID, "Company"),
            (By.ID, "Newsletter"),
            (By.ID, "Password"),
            (By.ID, "ConfirmPassword")
        ]

        for by, value in fields_to_check:
            self.assertTrue(wait.until(EC.visibility_of_element_located((by, value))), f"Field {value} is not visible.")

        # Check Register button is visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.ID, "register-button"))), "Register button is not visible.")

        # Check footer is visible
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer"))), "Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()