import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        # Quit the WebDriver session
        self.driver.quit()

    def test_ui_components_on_register_page(self):
        driver = self.driver
        driver.get("http://max/register?returnUrl=%2F")
        wait = WebDriverWait(driver, 20)

        # Verify header exists
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not found or not visible")

        # Verify register button exists
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-next-step-button")))
        except:
            self.fail("Register button is not found or not visible")

        # Verify register form fields
        fields = ["FirstName", "LastName", "Email", "Password", "ConfirmPassword"]
        for field_id in fields:
            try:
                field = wait.until(EC.visibility_of_element_located((By.ID, field_id)))
            except:
                self.fail(f"Form field with ID '{field_id}' is not found or not visible")

        # Verify the newsletter checkbox
        try:
            newsletter_checkbox = wait.until(EC.visibility_of_element_located((By.ID, "Newsletter")))
        except:
            self.fail("Newsletter checkbox is not found or not visible")

        # Verify footer exists
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not found or not visible")

if __name__ == "__main__":
    unittest.main()