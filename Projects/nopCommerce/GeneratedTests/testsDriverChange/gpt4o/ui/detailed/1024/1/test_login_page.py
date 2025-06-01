import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        # you can add more options as needed
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except:
            self.fail("Header is missing")

        # Check footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except:
            self.fail("Footer is missing")

        # Check login page title
        try:
            page_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title"))).text
            self.assertEqual(page_title, "Welcome, Please Sign In!")
        except:
            self.fail("Login page title is incorrect or missing")

        # Check presence of email input
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
        except:
            self.fail("Email input is missing")

        # Check presence of password input
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        except:
            self.fail("Password input is missing")

        # Check presence of login button and interact
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            login_button.click()
        except:
            self.fail("Login button is missing")

        # Check presence of register button
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        except:
            self.fail("Register button is missing")

        # Check presence of 'Forgot password?' link
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot password?")))
        except:
            self.fail("'Forgot password?' link is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()