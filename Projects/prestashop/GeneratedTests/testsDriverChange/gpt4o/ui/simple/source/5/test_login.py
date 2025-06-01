import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_UI_elements_presence(self):
        driver = self.driver

        # Check header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or visible")

        # Check email input field presence
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except:
            self.fail("Email input field is not present or visible")
        
        # Check password input field presence
        try:
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except:
            self.fail("Password input field is not present or visible")
        
        # Check Sign In button presence
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except:
            self.fail("Sign In button is not present or visible")

        # Check forgot password link presence
        try:
            forgot_password_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot your password?")))
        except:
            self.fail("Forgot password link is not present or visible")

        # Check Sign In link presence in navigation
        try:
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign In link in navigation is not present or visible")

        # Check main menu links presence
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")))
        except:
            self.fail("Home link is not present or visible")
        
        try:
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
        except:
            self.fail("Clothes link is not present or visible")
        
        try:
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
        except:
            self.fail("Accessories link is not present or visible")

        try:
            art_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Art link is not present or visible")

        try:
            register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Register link is not present or visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()