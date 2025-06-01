from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import Assertions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WaitForSeconds

def setUp(self):
    # Create a new WebDriver instance using ChromeDriver managed by webdriver-manager.
    self.driver = webdriver.Chrome()
    # Navigate to the website URL provided in the test scenario.
    self.driver.get("http://max/")
    
class TestLoginScenario(unittest.TestCase):
    def test_login_scenario(self):
        # Step 1: Open the home page.
        Assertions.assertTrue(self.driver.title(), "Home Page")
        
        # Step 2: Click the "Login" button in the top navigation.
        login_button = WebDriverWait(self.driver, 20).until(
            presence_of_element_located((By.XPATH, "//a[contains(text()='Login')]"))
        )
        login_button.click()
        
        # Step 3: Wait until the login page loads fully.
        Assertions.assertTrue(self.driver.title(), "Login Page")
        
        # Step 4: Fill in the email and password fields using the provided credentials.
        email_field = WebDriverWait(self.driver, 20).until(
            element_to_be_clickable((By.XPATH, "//input[contains(@name='Email')]"))
        )
        email_field.send_keys("admin@admin.com")
        password_field = WebDriverWait(self.driver, 20).until(
            element_to_be_clickable((By.XPATH, "//input[contains(@name='Password')]"))
        )
        password_field.send_keys("admin")
        
        # Step 5: Click the login button.
        login_button = WebDriverWait(self.driver, 20).until(
            element_to_be_clickable((By.XPATH, "//button[contains(@class='login-button')]"))
        )
        login_button.click()
        
        # Step 6: Verify that the user is logged in by checking the "Log out" button
        #         is present in the top navigation.
        logout_button = WebDriverWait(self.driver, 20).until(
            presence_of_element_located((By.XPATH, "//a[contains(text()='Log out')]"))
        )
        self.assertTrue(logout_button.is_displayed())
        
def tearDown(self):
    # Close the WebDriver instance after testing completion.
    self.driver.quit()

if __name__ == '__main__':
    unittest.main()