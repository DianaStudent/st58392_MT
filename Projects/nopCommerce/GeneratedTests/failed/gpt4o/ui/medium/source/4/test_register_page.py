from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/register?returnUrl=%2F')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header links
        try:
            header_links = [
                ('Register', '/register?returnUrl=%2F'),
                ('Log in', '/login?returnUrl=%2F'),
                ('Wishlist', '/wishlist'),
                ('Shopping cart', '/cart')
            ]
            for link_text, href in header_links:
                link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, link_text)))
                self.assertEqual(link.get_attribute('href'), f'http://max{href}')
        except Exception as e:
            self.fail(f"Header links are not present or not correct: {str(e)}")

        # Check search box
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
            self.assertIn("Search store", search_box.text)
        except Exception as e:
            self.fail(f"Search box is not present or visible: {str(e)}")

        # Check registration form fields
        try:
            form_fields = {
                'FirstName': 'First name',
                'LastName': 'Last name',
                'Email': 'Email',
                'Password': 'Password',
                'ConfirmPassword': 'Confirm password'
            }
            for field_id, label_text in form_fields.items():
                label = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//label[@for='{field_id}']")))
                self.assertEqual(label.text, f"{label_text}:")
        except Exception as e:
            self.fail(f"Registration form fields are not present or not correct: {str(e)}")

        # Check buttons
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'register-button')))
            self.assertEqual(register_button.get_attribute('type'), 'submit')
        except Exception as e:
            self.fail(f"Register button is not present or not correct: {str(e)}")

        # Interact with search box
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            search_input.send_keys('test')
            search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-box-button')))
            search_button.click()
            self.wait.until(EC.url_contains('search?q=test'))
        except Exception as e:
            self.fail(f"Search functionality is not working: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()