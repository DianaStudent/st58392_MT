import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_login_medium(self):
        # Click the "Login" link
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='master-column-wrapper']//button[@class='button-1 register-button']")))
        login_link.click()

        # Wait for the login page to load and enter email and password
        self.driver.get("http://max/login")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "__RequestVerificationToken")))

        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@class='email' and @data-val-required='Please enter your email']")))
        password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
        email_input.send_keys("admin@admin.com")
        password_input.send_keys("admin")

        # Click the login button to submit the form
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-primary']")))
        login_button.click()

        # Verify that the user is logged in by checking the "Log out" button is present in the top navigation
        logout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/Admin' and @class='administration']")))
        self.assertEqual(logout_button.text, 'Administration')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()