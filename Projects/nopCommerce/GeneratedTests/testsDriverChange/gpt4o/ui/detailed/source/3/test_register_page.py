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
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_registration_page(self):
        driver = self.driver
        driver.get('http://max/register?returnUrl=%2F')

        # Check structural elements
        self.check_element_visibility(By.CLASS_NAME, 'header')
        self.check_element_visibility(By.CLASS_NAME, 'footer')

        # Check input fields and labels
        self.check_element_visibility(By.ID, 'FirstName')
        self.check_element_visibility(By.ID, 'LastName')
        self.check_element_visibility(By.ID, 'Email')
        self.check_element_visibility(By.ID, 'Password')
        self.check_element_visibility(By.ID, 'ConfirmPassword')

        # Check radio buttons and checkbox
        self.check_element_visibility(By.ID, 'gender-male')
        self.check_element_visibility(By.ID, 'gender-female')
        self.check_element_visibility(By.ID, 'Newsletter')

        # Check buttons
        self.check_element_visibility(By.ID, 'register-button')
        self.check_element_visibility(By.ID, 'newsletter-subscribe-button')

        # Interaction with buttons
        self.wait.until(EC.element_to_be_clickable((By.ID, 'register-button'))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, 'newsletter-subscribe-button'))).click()

        # Check page title
        self.assertEqual(driver.title, "Your store. Register")

    def check_element_visibility(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(element.is_displayed())
        except Exception as e:
            self.fail(f"Element with locator {value} not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()