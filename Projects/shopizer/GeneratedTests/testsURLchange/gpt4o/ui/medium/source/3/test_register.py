import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

        # Check login form fields
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
        country_select = wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))

        # Check button
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Register']")))

        # Interact with button and check UI updates
        register_button.click()
        # Example: Check if form submission message appears, or URL changes, this step depends on exact behavior
        # For example, if submission message: 
        # submission_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "submission-message-class")))
        # self.assertIn("expected text", submission_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()