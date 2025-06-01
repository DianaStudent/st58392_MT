import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/login")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        except:
            self.fail("Header is missing")

        # Verify footer is present
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer is missing")

        # Verify login tab and form
        try:
            login_tab = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-register-tab-list")))
            username_input = driver.find_element(By.NAME, "username")
            password_input = driver.find_element(By.NAME, "loginPassword")
        except:
            self.fail("Login tab or input fields are missing")

        # Verify buttons
        try:
            remember_me_checkbox = driver.find_element(By.XPATH, "//input[@type='checkbox']")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Buttons are missing")

        # Check interaction
        try:
            accept_cookies_button.click()
        except:
            self.fail("Failed to click accept cookies button")

        try:
            remember_me_checkbox.click()
            assert remember_me_checkbox.is_selected(), "Checkbox not selected"
        except:
            self.fail("Failed to interact with the checkbox")

        # Assert navigation links are present
        try:
            nav_links = driver.find_elements(By.XPATH, "//nav//a")
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present")
        except:
            self.fail("Navigation links are missing or incorrect")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()