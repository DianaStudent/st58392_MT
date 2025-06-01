import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        # Set up the browser using WebDriverManager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/registration")
        self.driver.maximize_window()

    def test_page_elements(self):
        driver = self.driver

        # Verify that header, footer, and navigation are visible
        header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
        footer = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))
        nav = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))

        # Check presence and visibility of input fields
        firstname_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-firstname")))
        lastname_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-lastname")))
        email_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-email")))

        # Password with toggle button
        password_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-password")))
        show_password_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[data-action='show-password']")))

        # Additional fields
        birthday_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "field-birthday")))

        # Checkboxes
        optin_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "optin")))
        psgdpr_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "psgdpr")))
        newsletter_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "newsletter")))
        customer_privacy_checkbox = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "customer_privacy")))

        # Buttons
        save_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))

        # Interacting with elements
        firstname_input.send_keys("John")
        lastname_input.send_keys("Doe")
        email_input.send_keys("john.doe@example.com")
        password_input.send_keys("Password123")
        birthday_input.send_keys("01/01/1985")
        optin_checkbox.click()
        psgdpr_checkbox.click()
        newsletter_checkbox.click()
        customer_privacy_checkbox.click()
        show_password_button.click()

        # Submit the form
        save_button.click()

        # Assert that all essential components are present
        essential_elements = [header, footer, nav, firstname_input, lastname_input, email_input,
                              password_input, birthday_input, optin_checkbox, psgdpr_checkbox, 
                              newsletter_checkbox, customer_privacy_checkbox, save_button]
        for element in essential_elements:
            if not element.is_displayed():
                self.fail(f'Required UI element not found or not visible: {element}')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()