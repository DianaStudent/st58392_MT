import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/login')  # Open the main page
        self.wait = WebDriverWait(self.driver, 20)  # WebDriverWait with a timeout of 20 seconds

    def test_presence_of_ui_elements(self):
        try:
            # Check for presence and visibility of navigation links
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            # Check for presence and visibility of login form elements
            login_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()=' Login']")))
            username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button/span[text()='Login']")))

            # Interact with an element and check that the UI updates visually
            login_button.click()
            
        except Exception as e:
            self.fail(f"Element check failed: {str(e)}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()