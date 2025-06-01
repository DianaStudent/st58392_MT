import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        try:
            header_elements = [
                (By.LINK_TEXT, "Register"),
                (By.LINK_TEXT, "Log in"),
                (By.LINK_TEXT, "Wishlist"),
                (By.LINK_TEXT, "Shopping cart"),
                (By.LINK_TEXT, "Home page"),
                (By.LINK_TEXT, "New products"),
                (By.LINK_TEXT, "Search"),
                (By.LINK_TEXT, "My account"),
                (By.LINK_TEXT, "Blog"),
                (By.LINK_TEXT, "Contact us")
            ]
            for by, value in header_elements:
                element = wait.until(EC.visibility_of_element_located((by, value)))
                self.assertIsNotNone(element, f"Header element {value} not found or not visible.")

            # Check form fields
            form_field_ids = ['FirstName', 'LastName', 'Email', 'Password', 'ConfirmPassword']
            for field_id in form_field_ids:
                element = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
                self.assertIsNotNone(element, f"Form field {field_id} not found or not visible.")

            # Check the register button
            register_button = wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            self.assertIsNotNone(register_button, "Register button not found or not visible.")

        except Exception as e:
            self.fail(f"Test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()