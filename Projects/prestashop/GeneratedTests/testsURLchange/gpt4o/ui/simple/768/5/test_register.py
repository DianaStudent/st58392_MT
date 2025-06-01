import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegistrationPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header)
        except:
            self.fail("Header not found or not visible")

        # Check form fields
        try:
            form = self.wait.until(EC.visibility_of_element_located((By.ID, "customer-form")))
            self.assertIsNotNone(form)

            social_title_field = form.find_element(By.NAME, "id_gender")
            firstname_field = form.find_element(By.ID, "field-firstname")
            lastname_field = form.find_element(By.ID, "field-lastname")
            email_field = form.find_element(By.ID, "field-email")
            password_field = form.find_element(By.ID, "field-password")
            terms_checkbox = form.find_element(By.NAME, "psgdpr")
            privacy_checkbox = form.find_element(By.NAME, "customer_privacy")

            self.assertIsNotNone(social_title_field)
            self.assertIsNotNone(firstname_field)
            self.assertIsNotNone(lastname_field)
            self.assertIsNotNone(email_field)
            self.assertIsNotNone(password_field)
            self.assertIsNotNone(terms_checkbox)
            self.assertIsNotNone(privacy_checkbox)
        except:
            self.fail("Form fields not found or not visible")

        # Check submit button
        try:
            submit_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
            self.assertIsNotNone(submit_button)
        except:
            self.fail("Submit button not found or not visible")

        # Check footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer)
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()