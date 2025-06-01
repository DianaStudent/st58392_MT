import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver

        # Wait for header to be visible
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
        except:
            self.fail("Header is not visible")

        # Check visibility of login form fields
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
        except:
            self.fail("Email input field is not visible")

        try:
            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "loginPassword"))
            )
        except:
            self.fail("Password input field is not visible")

        # Check visibility and presence of remember me checkbox and label
        try:
            remember_me_checkbox = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//input[@type='checkbox']"))
            )
        except:
            self.fail("Remember me checkbox is not visible")

        try:
            remember_me_label = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "label.ml-10"))
            )
        except:
            self.fail("Remember me label is not visible")
        
        # Check that 'Login' button is visible and clickable
        try:
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[span='Login']"))
            )
            ActionChains(driver).move_to_element(login_button).click().perform()
        except:
            self.fail("Login button is not clickable")

        # Wait for footer to be visible
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "footer"))
            )
        except:
            self.fail("Footer is not visible")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()