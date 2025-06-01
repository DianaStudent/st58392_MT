import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://max/")

    def test_login(self):
        email_input = driver.find_element_by_name("Email")
        password_input = driver.find_element_by_name("Password")
        
        # Enter the email and password
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")
        
        # Click the login button to submit the form
        login_button = driver.find_element_by_css_selector(".button-1.login-button")
        login_button.click()
        
        # Wait for 20 seconds before checking if the "Log out" button is present
        WebDriverWait(driver, 20).until(
            lambda x: self.assertTrue(x.find_element_by_link_text("Log out").is_displayed())
        )
    
    @classmethod
    def tearDown(self):
        driver.quit()

if __name__ == '__main__':
    unittest.main()