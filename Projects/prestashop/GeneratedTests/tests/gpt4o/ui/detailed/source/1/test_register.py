import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_presence_of_ui_elements(self):
        driver = self.driver

        # Check presence of header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not present or visible.")

        # Check presence of footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not present or visible.")

        # Check presence of form and its fields
        try:
            form = self.wait.until(EC.visibility_of_element_located((By.ID, 'customer-form')))
            firstname = form.find_element(By.ID, 'field-firstname')
            lastname = form.find_element(By.ID, 'field-lastname')
            email = form.find_element(By.ID, 'field-email')
            password = form.find_element(By.ID, 'field-password')
            submit_button = form.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        except:
            self.fail("Form fields or submit button are not present or visible.")

        # Check presence of labels
        try:
            create_account_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Create an account']")))
        except:
            self.fail("Create account header is not present or visible.")

        # Check presence of other important sections like newsletter subscription
        try:
            newsletter_section = self.wait.until(EC.visibility_of_element_located((By.ID, 'blockEmailSubscription_displayFooterBefore')))
        except:
            self.fail("Newsletter subscription section is not present or visible.")

        # Interact with UI elements
        try:
            firstname.send_keys('Test')
            lastname.send_keys('User')
            email.send_keys('test@example.com')
            password.send_keys('TestPassword123')
            submit_button.click()
        except Exception as e:
            self.fail(f"Failed to interact with form elements: {str(e)}")

        # Confirm visual reaction
        # This needs app-specific logic, e.g. check success message or redirection

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()