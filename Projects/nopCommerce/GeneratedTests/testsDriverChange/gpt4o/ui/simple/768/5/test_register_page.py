import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegisterPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box")))

            # Check menu
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))

            # Check Register form elements
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))

            # Check Register button
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

            # Additional checks for other elements (e.g., gender radio buttons)
            wait.until(EC.visibility_of_element_located((By.ID, "gender-male")))
            wait.until(EC.visibility_of_element_located((By.ID, "gender-female")))

        except Exception as e:
            self.fail(f"UI element(s) not found or visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()