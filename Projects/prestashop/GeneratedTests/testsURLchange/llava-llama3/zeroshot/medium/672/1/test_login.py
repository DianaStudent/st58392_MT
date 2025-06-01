import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.text_fields import TextFields

class TestLoginScenario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_login_scenario(self):
        # Act - Navigate to the home page
        self.driver.get('http://localhost:8080/en/')
        
        # Assert - Check if the login menu is present
        login_menu = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector("li[data-name='login']")
        )
        
        # Act - Click on the login menu
        login_menu.find_elements_by_css_selector("a")[1].click()
        
        # Assert - Check if the login page is loaded
        self.assertTrue('Login' in self.driver.title)
        
        # Act - Fill in the email and password fields
        email_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("email")
        )
        email_field.send_keys("test@user.com")
        
        password_field = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_name("password")
        )
        password_field.send_keys("test@user1")

        # Act - Submit the login form
        self.driver.find_element_by_css_selector("form").submit()

        # Assert - Check if login was successful by checking for the presence of "Sign out" in the top bar
        signout_button = WebDriverWait(self.driver, 20).until(
            lambda x: x.find_element_by_css_selector("a[data-name='sign-out']")
        )
        
        self.assertTrue(signout_button is not None)
        
if __name__ == '__main__':
    unittest.main()