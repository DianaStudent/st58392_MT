from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_login(self):
        # Step 1: Open the home page.
        self.driver.get('http://localhost:8080/en/')

        # Step 2: Click on the login link in the top menu.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[href$="login"]'))).click()

        # Step 3: Wait for the login page to load.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))

        # Step 4: Fill in the email and password fields.
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        self.assertEqual(email_field.get_attribute('data-name'), 'Email')  
        email_field.send_keys("test@user.com")

        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'password')))
        self.assertEqual(password_field.get_attribute('data-name'), 'Password')
        password_field.send_keys("test@user1")

        # Step 5: Submit the login form.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]'))).click()

        # Step 6: Verify that login was successful by checking for the presence of "Sign out" in the top bar.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[text()="Sign out"]')))
        sign_out_button = self.driver.find_element(By.XPATH, '//a[text()="Sign out"]')
        self.assertEqual(sign_out_button.get_attribute('data-name'), 'Sign out')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()