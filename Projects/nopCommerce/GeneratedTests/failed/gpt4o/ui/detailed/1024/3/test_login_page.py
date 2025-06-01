from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/login?returnUrl=%2F")
        
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header")))
        self.assertIsNotNone(header, 'Header is not visible.')

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))
        self.assertIsNotNone(footer, 'Footer is not visible.')

        # Check login form elements
        email_input = wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        password_input = wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        login_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button")))

        self.assertIsNotNone(email_input, 'Email input is not visible.')
        self.assertIsNotNone(password_input, 'Password input is not visible.')
        self.assertIsNotNone(login_button, 'Login button is not visible.')

        # Check Register button
        register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.register-button")))
        self.assertIsNotNone(register_button, 'Register button is not visible.')

        # Check that the search bar is present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))
        
        self.assertIsNotNone(search_input, 'Search input is not visible.')
        self.assertIsNotNone(search_button, 'Search button is not visible.')

        # Interact with the login button to test visual feedback
        login_button.click()
        
        # Check if an alert pops up for empty fields (indicating UI feedback)
        alert_present = EC.alert_is_present()(driver)
        self.assertTrue(alert_present, 'No alert for empty login fields.')
        
        if alert_present:
            driver.switch_to.alert.accept()

if __name__ == "__main__":
    unittest.main()