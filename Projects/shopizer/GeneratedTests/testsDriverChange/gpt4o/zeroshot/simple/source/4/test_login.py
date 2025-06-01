import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestLoginProcess(unittest.TestCase):
    def setUp(self):
        # Setup Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run headless if desired
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Path to the chromedriver executable
        service = Service('/path/to/chromedriver')

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get('http://localhost/')

    def test_login(self):
        driver = self.driver

        try:
            # Accept cookies
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            ).click()

            # Click on account icon to open menu
            account_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.account-setting .account-setting-active'))
            )
            account_icon.click()

            # Click on Login link
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, 'Login'))
            )
            login_link.click()

            # Fill in email and password
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, 'username'))
            )
            password_input = driver.find_element(By.NAME, 'loginPassword')

            email_input.send_keys('test2@user.com')
            password_input.send_keys('test**11')

            # Click on Login button
            login_button = driver.find_element(By.CSS_SELECTOR, '.button-box button')
            login_button.click()

            # Check if redirected to '/my-account'
            WebDriverWait(driver, 20).until(
                EC.url_contains('/my-account')
            )
        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()