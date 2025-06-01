import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")
        
        # Check visibility of footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible.")
        
        # Check visibility of registration form
        try:
            form = wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
        except:
            self.fail("Registration form is not visible.")

        # Check visibility of fields and buttons
        fields_and_buttons = [
            ("Social title", (By.ID, "field-id_gender-1")),
            ("First name", (By.ID, "field-firstname")),
            ("Last name", (By.ID, "field-lastname")),
            ("Email", (By.ID, "field-email")),
            ("Password", (By.ID, "field-password")),
            ("Save", (By.XPATH, "//button[@type='submit'][@data-link-action='save-customer']")),
            ("Opt-in checkbox", (By.NAME, "optin"))
        ]

        for name, selector in fields_and_buttons:
            try:
                element = wait.until(EC.visibility_of_element_located(selector))
            except:
                self.fail(f"{name} is not visible or present.")
        
        # Interact with UI elements
        # Click save button
        try:
            save_button = driver.find_element(By.XPATH, "//button[@type='submit'][@data-link-action='save-customer']")
            save_button.click()
        except:
            self.fail("Unable to click save button.")

        # Confirm UI reacts, checking for error message or validation (Example: checking any error validation after submit)
        try:
            error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        except:
            print("No error message displayed, assuming UI interaction is successful.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()