from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # Replace with your preferred browser

    def test_login_successfully(self):
        # Home page before login check
        url = "http://max/"  # Replace with the URL of the website
        self.driver.get(url)
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "input[name=__RequestVerificationToken]")))

        # Login page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".login-page")))
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, ".login-page").text, 'Welcome, Please Sign In!')

        # Enter email and password
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.email[name=Email]")))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=password][name=Password]")))

        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click login button
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-button")))
        login_button.click()

        # After login check
        self.assertEqual(self.driver.find_element(By.CSS_SELECTOR, "a.administration[href=/Admin]").text, 'Administration')
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type=button][class=admin-logout-button]"))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()