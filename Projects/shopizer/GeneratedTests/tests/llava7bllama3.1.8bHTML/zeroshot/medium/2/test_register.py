from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/")

    def test_registration(self):
        # Step 1: Open the home page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Account")))

        # Step 2: Click on the account button and select "Register"
        self.driver.find_element(By.LINK_TEXT, "Account").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        self.driver.find_element(By.LINK_TEXT, "Register").click()

        # Step 3: Fill in the registration form
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        email_input = self.driver.find_element(By.ID, 'email')
        if not email_input.get_attribute('value'):
            email_input.send_keys('test_email@shopizer.com')

        password_input = self.driver.find_element(By.ID, 'password')
        if not password_input.get_attribute('value'):
            password_input.send_keys('test**11')

        first_name_input = self.driver.find_element(By.ID, 'first_name')
        if not first_name_input.get_attribute('value'):
            first_name_input.send_keys('Test')

        last_name_input = self.driver.find_element(By.ID, 'last_name')
        if not last_name_input.get_attribute('value'):
            last_name_input.send_keys('User')

        # Step 4: Select a country and a region/state
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'country')))
        self.driver.find_element(By.ID, 'country').send_keys('United States')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'state_id')))

        # Step 5: Submit the registration form
        self.driver.find_element(By.NAME, 'commit').click()

        try:
            # Wait for redirect and confirm success by checking if the current URL includes "/my-account"
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            self.assertIn('/my-account', self.driver.current_url)
        except TimeoutException:
            self.fail('Registration failed')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()