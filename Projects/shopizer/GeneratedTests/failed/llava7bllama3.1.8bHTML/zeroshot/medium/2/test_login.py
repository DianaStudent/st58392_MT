from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_login(self):
        # Click the account icon in the top navigation bar
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-toggle='dropdown']"))).click()

        # Click the "Login" link
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Fill in the email and password fields
        self.driver.find_element(By.NAME, 'email').send_keys('test2@user.com')
        self.driver.find_element(By.NAME, 'password').send_keys('test**11')

        # Submit the login form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()

        # Confirm success by checking that the browser is redirected to a page with "/my-account" in the URL.
        url = self.driver.current_url
        self.assertIn('/my-account', url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()