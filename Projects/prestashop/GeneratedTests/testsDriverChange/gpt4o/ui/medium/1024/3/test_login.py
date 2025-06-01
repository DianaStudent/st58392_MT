import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check presence of the navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            
            # Check presence of login form elements
            email_input = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
            password_input = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
            sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))

            # Check presence of registration link
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))

            # Interact with the sign in button
            sign_in_button.click()

            # Assume an invalid login attempt, check for error message visibility
            error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert-danger")))

        except Exception as e:
            self.fail(f"Test failed due to missing element or interaction error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()