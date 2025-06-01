import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestLogin(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='top-nav']/a[@href='/my-account']")))

    def test_login(self):
        # Click on the account icon/button
        account_button = self.driver.find_element(By.XPATH, "//div[@class='top-nav']/a[@href='/my-account']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-menu']/ul/li/a[@href='/login']")))
        account_button.click()

        # Wait for the dropdown and click the "Login" link
        login_link = self.driver.find_element(By.XPATH, "//div[@class='dropdown-menu']/ul/li/a[@href='/login']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@id='login-form']")))
        login_link.click()

        # Wait for the login form to appear
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//form[@id='login-form']")), 1)

        # Fill in the username and password fields using credentials
        email_field = self.driver.find_element(By.XPATH, "//input[@name='email']")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        email_field.send_keys('test2@user.com')
        password_field = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_field.send_keys('test**11')

        # Click the login button
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Wait for redirection or page update
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'My Account')]")))

        # Confirm successful login by checking that the current URL contains "/my-account"
        self.assertIn('/my-account', self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()