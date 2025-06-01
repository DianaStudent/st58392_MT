import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_interactive(self):
        driver = self.driver
        wait = self.wait

        # Verify navigation links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Navigation links are not visible")

        # Verify the presence of the login/register button
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Account buttons are not visible or not clickable")

        # Verify form fields on the login/register page by navigating to the register page
        driver.get("http://localhost/register")
        try:
            email_input = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
            repeat_password_input = wait.until(EC.visibility_of_element_located((By.NAME, "repeatPassword")))
            first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            country_select = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "select")))
            state_input = wait.until(EC.visibility_of_element_located((By.NAME, "stateProvince")))
            register_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button")))
        except:
            self.fail("Register form fields are not visible or missing")

        # Interact with an element and ensure no errors
        try:
            register_button.click()
        except:
            self.fail("Register button is not clickable or caused an error")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()