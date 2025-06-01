from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = ChromeService(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.get("http://max/")

    def setUp(self):
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements_existence(self):
        # Check for header presence
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header')))
        self.assertTrue(header.is_displayed(), "Header is not visible on the page.")
        
        # Check for footer presence
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible on the page.")
        
        # Check for login link presence
        login_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-login')))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible on the page.")

        # Check for register link presence
        register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.ico-register')))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible on the page.")
        
        # Check for search box presence
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible on the page.")
        
        # Check for navigation menu presence
        navigation_menu = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.top-menu')))
        self.assertTrue(navigation_menu.is_displayed(), "Navigation menu is not visible on the page.")

    def test_login_interaction(self):
        self.driver.get("http://max/login?returnUrl=%2F")

        # Check and interact with Email input
        email_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Email')))
        self.assertTrue(email_input.is_displayed(), "Email input is not visible.")
        
        # Check and interact with Password input
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'Password')))
        self.assertTrue(password_input.is_displayed(), "Password input is not visible.")
        
        # Check for Login button presence and interaction
        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.button-1.login-button')))
        self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        login_button.click()

        # Check for error notifications or validation messages
        error_notification = self.driver.find_elements(By.ID, 'dialog-notifications-error')
        if error_notification:
            self.assertTrue(error_notification[0].is_displayed(), "Error notifications should be visible after failed login attempt.")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()