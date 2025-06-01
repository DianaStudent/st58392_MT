import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class RegisterTest(unittest.TestCase):
    driver = None
    username = None

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        time.sleep(1)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_register(self):
        email = "test_user_" + str(random.randint(1000, 100000)) + "@user.com"
        self.username = "Test User" + str(random.randint(1000, 10000))

        try:
            # Open the homepage
            time.sleep(1)

            # Click the login link from the top navigation
            login_link = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//a[@class='nav-link']"))), 'Login Link not found')

            # Move to the login page and click on the register link (e.g. "No account? Create one here")
            register_link = WebDriverWait(self.driver, 20).until(
                EC.element_located((By.XPATH, "//a[contains(text(), 'No account? Create one here')]"))),
                'Register Link not found'
            )
            register_link.click()

            # Fill in the following fields using credentials:
            time.sleep(1)

            gender = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//label[@data-name='gender']")))
            gender.click()
            time.sleep(1)

            first_name_input = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@id='firstName']")))
            first_name_input.send_keys(self.username)
            time.sleep(1)

            last_name_input = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@id='lastName']")))
            last_name_input.send_keys("User")
            time.sleep(1)

            email_input = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@id='email']")))
            email_input.send_keys(email)
            time.sleep(1)

            password_input = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//input[@id='password']")))
            password_input.send_keys("test@user1")
            time.sleep(1)

            checkbox1 = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//label[@data-name='privacy']")))
            checkbox1.click()
            time.sleep(1)

            checkbox2 = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//label[@data-name='newsletter']")))
            checkbox2.click()
            time.sleep(1)

            checkbox3 = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//label[@data-name='terms']")))
            checkbox3.click()
            time.sleep(1)

            submit_button = WebDriverWait(self.driver, 20).until(EC.element_located((By.XPATH, "//button[@id='submit']")))
            submit_button.click()

            # Wait for the redirect after login
            time.sleep(3)

            # Confirm that login was successful by checking that:
            self.assertTrue(
                self.driver.current_url != "http://localhost:8080/en/login",
                'Failed to get redirected to homepage'
            )
            self.assertTrue(
                self.driver.page_source.find('Sign out') is not None,
                'Sign out button missing on top navigation'
            )

            time.sleep(3)

        except Exception as e:
            print(f'Error occurred: {str(e)}')
            raise

if __name__ == '__main__':
    unittest.main()