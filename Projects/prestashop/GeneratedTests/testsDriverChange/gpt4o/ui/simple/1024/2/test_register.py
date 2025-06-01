import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Tear down the WebDriver
        self.driver.quit()

    def test_registration_page_elements(self):
        driver = self.driver

        try:
            # Check for header
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header.is_displayed())
            
            # Check for main form fields
            firstname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-firstname")))
            self.assertTrue(firstname.is_displayed())
            
            lastname = self.wait.until(EC.visibility_of_element_located((By.ID, "field-lastname")))
            self.assertTrue(lastname.is_displayed())

            email = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            self.assertTrue(email.is_displayed())
            
            password = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            self.assertTrue(password.is_displayed())
            
            birthdate = self.wait.until(EC.visibility_of_element_located((By.ID, "field-birthday")))
            self.assertTrue(birthdate.is_displayed())

            # Check for buttons and links
            register_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-link-action='save-customer']")))
            self.assertTrue(register_button.is_displayed())

            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in instead!")))
            self.assertTrue(login_link.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

if __name__ == '__main__':
    unittest.main()