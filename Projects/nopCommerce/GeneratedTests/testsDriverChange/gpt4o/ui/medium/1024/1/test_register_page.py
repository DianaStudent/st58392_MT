import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_elements_presence_and_interaction(self):
        driver = self.driver

        # Check presence and visibility of header links
        try:
            header_links = driver.find_element(By.CLASS_NAME, 'header-links')
            self.assertTrue(header_links.is_displayed())
        except Exception as e:
            self.fail(f"Header links not found or not visible: {str(e)}")

        # Check presence and visibility of register form fields
        form_fields = ['gender', 'FirstName', 'LastName', 'Email', 'Password', 'ConfirmPassword']
        for field_id in form_fields:
            try:
                element = driver.find_element(By.ID, field_id)
                self.assertTrue(element.is_displayed())
            except Exception as e:
                self.fail(f"Form field {field_id} not found or not visible: {str(e)}")

        # Check presence and visibility of the register button
        try:
            register_button = driver.find_element(By.ID, 'register-button')
            self.assertTrue(register_button.is_displayed())
        except Exception as e:
            self.fail(f"Register button not found or not visible: {str(e)}")

        # Interact with the newsletter checkbox
        try:
            newsletter_checkbox = driver.find_element(By.ID, 'Newsletter')
            self.assertTrue(newsletter_checkbox.is_displayed())
            newsletter_checkbox.click()

            # Check that checkbox toggles
            self.assertFalse(newsletter_checkbox.is_selected(), "Checkbox should not be selected.")
        except Exception as e:
            self.fail(f"Newsletter checkbox not found or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()