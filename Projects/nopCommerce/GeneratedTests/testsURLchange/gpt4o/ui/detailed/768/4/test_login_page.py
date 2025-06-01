import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check visibility of header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is not visible on the login page.")
        
        # Check visibility of footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is not visible on the login page.")
        
        # Check the presence and visibility of form fields and buttons
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.register-button")))
        except:
            self.fail("Form fields or buttons are not visible on the login page.")
            
        # Check presence of labels
        email_label = driver.find_element(By.XPATH, "//label[@for='Email']")
        password_label = driver.find_element(By.XPATH, "//label[@for='Password']")
        self.assertTrue(email_label.is_displayed(), "Email label is not visible.")
        self.assertTrue(password_label.is_displayed(), "Password label is not visible.")
        
        # Interact with key elements
        driver.find_element(By.CLASS_NAME, "ico-register").click()
        
        # Confirm UI reaction by checking if navigated to the register page
        wait.until(EC.url_to_be("http://max/register?returnUrl=%2F"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()