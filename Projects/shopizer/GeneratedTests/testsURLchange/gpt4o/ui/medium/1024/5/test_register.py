import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/login")

    def test_ui_elements_presence_and_interactivity(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check that the logo and main menu links are present
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo img")))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")
        except Exception as e:
            self.fail(f"Main menu elements are not loaded: {e}")

        # Check that the login and register form fields are present
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")
        except Exception as e:
            self.fail(f"Login/Register form elements are not loaded: {e}")

        # Check interactivity: Click the Register button
        try:
            register_button.click()
            # Verify UI update (e.g., check for an alert, toast message, or heading change)
            # Here, assuming registration success shows a toast or makes input fields invisible
            WebDriverWait(driver, 10).until(
                EC.invisibility_of_element_located((By.NAME, "email")),
                "Expect email input to disappear on successful registration."
            )
        except Exception as e:
            self.fail(f"Failed to interact with the Register button: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()