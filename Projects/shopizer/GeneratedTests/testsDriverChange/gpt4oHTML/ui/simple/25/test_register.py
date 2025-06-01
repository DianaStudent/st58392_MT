import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):
    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check presence of header
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        if not header:
            self.fail("Header is not present.")
        
        # Check presence of navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        if not all([home_link, tables_link, chairs_link]):
            self.fail("One or more navigation links are not present.")
        
        # Check presence of account setting button
        account_setting_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-button")))
        if not account_setting_button:
            self.fail("Account setting button is not present.")
        
        # Check presence of login/register page elements
        login_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='login']/h4[contains(text(),'Login')]")))
        register_tab = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@data-rb-event-key='register' and contains(@class, 'active')]/h4[contains(text(),'Register')]")))
        
        if not all([login_tab, register_tab]):
            self.fail("Login/Register tab is not present.")
        
        # Ensure presence of form fields
        email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
        
        if not all([email_input, password_input, repeat_password_input]):
            self.fail("One or more form fields are not present.")
        
        # Check presence of the submit button
        register_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Register']]")))
        if not register_button:
            self.fail("Register button is not present.")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()