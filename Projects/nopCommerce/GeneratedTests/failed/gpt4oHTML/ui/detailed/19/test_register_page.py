from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://max/"

    def test_ui_elements(self):
        driver = self.driver

        # Load the registration page
        driver.get(f"{self.base_url}/register?returnUrl=%2F")

        # Validate presence and visibility of structural elements
        try:
            # Header
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            # Footer
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            # Main content
            self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
            # Navigation menu
            navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))

            # Check visibility of key buttons and links
            register_link = navigation.find_element(By.LINK_TEXT, "Register")
            self.assertTrue(register_link.is_displayed(), "Register link not visible")
            
            login_link = navigation.find_element(By.LINK_TEXT, "Log in")
            self.assertTrue(login_link.is_displayed(), "Login link not visible")
            
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_button.is_displayed(), "Search button not visible")

            # Check presence and visibility of form fields
            first_name = driver.find_element(By.ID, "FirstName")
            last_name = driver.find_element(By.ID, "LastName")
            email = driver.find_element(By.ID, "Email")
            password = driver.find_element(By.ID, "Password")
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            register_button = driver.find_element(By.ID, "register-button")

            # Ensure all form fields and related elements are visible
            for field_element in [first_name, last_name, email, password, confirm_password, register_button]:
                if not field_element.is_displayed():
                    self.fail(f"{field_element.get_attribute('id')} field is not visible")

            # Interaction: Enter data and click the Register button
            first_name.send_keys("John")
            last_name.send_keys("Doe")
            email.send_keys("john.doe@example.com")
            password.send_keys("password123")
            confirm_password.send_keys("password123")
            register_button.click()

            # Confirm UI reacts visually (e.g., redirect or show error message)
            self.wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        # Teardown: Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()