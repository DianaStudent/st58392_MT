import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements(self):
        try:
            # Check for navigation link 'Clothes'
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.ID, 'category-3')))
            self.assertTrue(clothes_link.is_displayed(), "Clothes link is not visible")

            # Check for navigation link 'Accessories'
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.ID, 'category-6')))
            self.assertTrue(accessories_link.is_displayed(), "Accessories link is not visible")

            # Check for navigation link 'Art'
            art_link = self.wait.until(EC.visibility_of_element_located((By.ID, 'category-9')))
            self.assertTrue(art_link.is_displayed(), "Art link is not visible")

            # Verify 'Create an Account' form fields
            firstname_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-firstname')))
            lastname_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-lastname')))
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-email')))
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'field-password')))

            self.assertTrue(firstname_input.is_displayed(), "First name input is not visible")
            self.assertTrue(lastname_input.is_displayed(), "Last name input is not visible")
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            # Verify 'Save' button in the form
            save_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.form-footer .btn-primary')))
            self.assertTrue(save_button.is_displayed(), "Save button is not visible")

            # Interact with 'Save' button to ensure UI behavior
            save_button.click()
            # Check for some indication of form processing (e.g., a spinner or success message, expecting failure here for illustration)
            # success_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.success-message')))
            # self.assertTrue(success_message.is_displayed(), "Success message is not visible after form submission")

        except Exception as e:
            self.fail(f"Test failed due to an unexpected error: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()