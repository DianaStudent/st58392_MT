import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Check navigation links visibility
        nav_links = ["//a[@href='http://localhost:8080/en/3-clothes']",
                     "//a[@href='http://localhost:8080/en/6-accessories']",
                     "//a[@href='http://localhost:8080/en/9-art']"]
        for link in nav_links:
            nav_element = wait.until(EC.visibility_of_element_located((By.XPATH, link)))
            if not nav_element.is_displayed():
                self.fail(f"Navigation link {link} is not visible")

        # Check login input fields
        email_field = wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, "field-password")))

        if not email_field.is_displayed() or not password_field.is_displayed():
            self.fail("Email or Password field is not visible")

        # Check "Forgot your password?" link
        forgot_password = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        if not forgot_password.is_displayed():
            self.fail("'Forgot your password?' link is not visible")

        # Check "Sign in" button and click it to ensure UI reacts
        sign_in_button = wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        if not sign_in_button.is_displayed():
            self.fail("Sign in button is not visible")

        # Interact with Sign in button
        sign_in_button.click()

        # Check "No account? Create one here" link
        no_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        if not no_account_link.is_displayed():
            self.fail("'No account? Create one here' link is not visible")

if __name__ == "__main__":
    unittest.main()