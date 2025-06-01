```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class RegisterTest(unittest.TestCase):
    def setUp(self):
        # Set up the driver to manage the Chrome browser.
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver

    def tearDown(self):
        # Close the browser after the test is completed.
        self.driver.quit()

    def test_register(self):
        # Open the home page.
        self.driver.get('http://localhost:8080/en/')

        # Click on the login link in the top menu.
        login_link = self.wait_for_element_located((By.XPATH, "//a[@data-name='login-link']"))
        login_link.click()

        # Click on the register link on the login page.
        register_link = self.wait_for_element_located((By.XPATH, "//a[@data-name='register-link']"))
        register_link.click()

        # Fill in the registration form fields:
        gender = Select(self.wait_for_element_located((By.XPATH, "//label[@data-name='gender']")))
        gender.select_by_value('m')
        self.wait_for_element_located((By.XPATH, "//label[@data-name='first-name']")))
        self.wait_for_element_located((By.XPATH, "//label[@data-name='last-name']")))
        self.wait_for_element_located((By.XPATH, "//input[@data-name='email']")))
        self.wait_for_element_located((By.XPATH, "//input[@data-name='password']")))
        self.wait_for_element_located((By.XPATH, "//input[@data-name='birthday']")))
        self.wait_for_element_located((By.XPATH, "//label[@data-name='terms-and-conditions']")))

        # Submit the form.
        submit_button = self.wait_for_element_located((By.XPATH, "//button[@data-name='submit-btn']"))
        submit_button.click()

        # Confirm success by checking for the presence of  "Sign out" in the top bar.
        sign_out_link = self.wait_for_element_located((By.XPATH, "//a[@data-name='sign-out-link']"))
        self.assertTrue(sign_out_link.is_displayed(), "Failed to find Sign Out link after submitting registration form.")

if __name__ == '__main__':
    unittest.main()
```