import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.keys import Key

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        # Open the home page.
        self.wait.until(EC.url_contains("http://localhost:8080/"))
        
        # Click on the account icon.
        self.wait.until(EC.element_located_by_selector("[data-toggle='modal'][data-target='#LoginModal']"))
        
        # Click the "Login" link to open the login form.
        self.wait.until(EC.element_located_by_selector("[data-dismiss='modal']"))

        # Fill in the email and password fields using credentials.
        self.wait.until(EC.presence_of_element_located(("[name=\"email\"]")))
        self.email = self.wait.until(EC.element_located_by_selector("[type='email']"))
        self.email.send_keys("test2@user.com")
        
        self.wait.until(EC.presence_of_element_located(("[name=\"password\"]")))
        self.password = self.wait.until(EC.element_located_by_selector("[type='password']"))
        self.password.send_keys("test**11")

        # Click the login button.
        self.wait.until(EC.element_located_by_selector("[type='submit']"))
        self.login_button = self.wait.until(EC.element_located_by_selector("[data-toggle=\"modal\" data-target=\"#LoginModal\"]"))
        
        # Wait for redirection or page update.
        self.wait.until(EC.url_contains("/my-account"))
        
        # Confirm successful login by verifying that the current URL contains "/my-account".
        self.assertTrue(EC.url_contains("/my-account").to_string().strip())
    
if __name__ == '__main__':
    unittest.main()