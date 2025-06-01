import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestRegisterPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        from webdriver_manager.chrome import ChromeDriverManager
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_register(self):
        self.driver.get("http://max/")  # replace with your app url

        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, '__RequestVerificationToken')))

        email = "test" + str(12345) + "@example.com"
        first_name = "John"
        last_name = "Doe"
        company = "Test Company"

        # Personal Details
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'FirstName'))).send_keys(first_name)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'LastName'))).send_keys(last_name)

        # Company Details
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'Company'))).send_keys(company)

        # Email and Password
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'Password'))).send_keys('test11')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'ConfirmPassword'))).send_keys('test11')

        # Email
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'Email')))
        email_input.clear()
        email_input.send_keys(email)

        # Newsletter
        newsletter_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'Newsletter')))

        # Submit Button
        register_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'register-button')))
        register_button.click()

        # Check if registration is successful
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.result')))

        result_text = self.driver.find_element(By.CSS_SELECTOR, '.result').text

        if "Your registration completed" not in result_text:
            self.fail("Registration was not successful")

if __name__ == '__main__':
    unittest.main()