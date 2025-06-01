from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost/login')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for logo
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo img')))

            # Check for navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))

            # Check for login tab
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[text()='Login']")))

            # Check for form fields
            wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'user-password')))

            # Check for buttons and links
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#rcc-confirm-button')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Forgot Password?')))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-box button[type="submit"]')))

        except Exception as e:
            self.fail(f"An element is missing or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()