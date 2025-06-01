import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        except:
            self.fail("Header is not present and visible.")

        # Check footer presence
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        except:
            self.fail("Footer is not present and visible.")

        # Check navigation menu
        try:
            navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        except:
            self.fail("Navigation menu is not present and visible.")

        # Check Register title
        try:
            title = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="page-title"]/h1[text()="Register"]')))
        except:
            self.fail("Register title is not present and visible.")

        # Check input fields
        input_fields = ['FirstName', 'LastName', 'Email', 'Password', 'ConfirmPassword']
        for field_id in input_fields:
            try:
                field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Input field {field_id} is not present and visible.")

        # Check buttons
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button')))
        except:
            self.fail("Buttons are not present and visible.")

        # Interact with Register button
        try:
            register_button.click()
        except:
            self.fail("Register button interaction failed.")

        # Additional visual check or interaction if needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()