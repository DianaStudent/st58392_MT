import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver

        # Verify header elements are visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible")

        # Verify footer elements are visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible")

        # Verify main form elements are visible
        try:
            form = self.wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
            input_firstname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            input_lastname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            input_email = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            input_password = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            input_birthday = self.wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
        except:
            self.fail("One or more form fields are not visible")

        # Check visibility of buttons and links
        try:
            save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
        except:
            self.fail("Save button is not visible")

        # Interact with the Password field
        try:
            password_field = driver.find_element(By.ID, "field-password")
            password_field.send_keys("testPassword")
            show_button = driver.find_element(By.CSS_SELECTOR, "button[data-action='show-password']")
            show_button.click()
        except:
            self.fail("Interaction with password field or button failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()