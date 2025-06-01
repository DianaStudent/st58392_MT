from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    @classmethod
    def setUp(self):
        driver_manager = ChromeDriverManager()
        driver_manager.download('https://chromedriver.chromium.org/downloads')
        self.driver = webdriver.Chrome(driver_manager.installer.get_chromedriver())

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        home_url = 'http://localhost:8080/en/'
        email = 'test@user.com'
        password = 'test@user1'

        # 1. Open the home page
        self.driver.get(home_url)

        # 2. Click on the login link in the top menu
        login_link = self.driver.find_element_by_tag_name('a')
        login_link.click()

        # Wait for the login page to load
        WebDriverWait(self.driver, 20).until(lambda x: "Sign out" in self.driver.page_source)

        # Fill in the email and password fields
        email_input = self.driver.find_element_by_id('email')
        password_input = self.driver.find_element_by_id('password')
        email_input.send_keys(email)
        password_input.send_keys(password)

        # Submit the login form
        self.driver.find_element_by_id('login-button').click()

        # Verify that login was successful by checking for the presence of "Sign out" in the top bar
        self.assertTrue("Sign out" in self.driver.page_source, "Login failed")

if __name__ == '__main__':
    unittest.main()