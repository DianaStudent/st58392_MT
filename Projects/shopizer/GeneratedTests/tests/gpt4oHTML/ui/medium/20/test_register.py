import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        except:
            self.fail("Home link is not visible.")

        try:
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        except:
            self.fail("Tables link is not visible.")

        try:
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Chairs link is not visible.")

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        except:
            self.fail("Header is not visible.")

        # Check login/register form
        driver.get("http://localhost/register")
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        except:
            self.fail("Email input is not visible on the register page.")
        
        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "password")))
        except:
            self.fail("Password input is not visible on the register page.")
        
        try:
            register_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[span[text()='Register']]")))
        except:
            self.fail("Register button is not visible on the register page.")

        # Interact with a button
        register_button.click()

        # Assert no errors occurred
        try:
            self.wait.until(EC.url_to_be("http://localhost/register"))
        except:
            self.fail("Unexpected URL after clicking register button or page load issue.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()