import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_register_user(self):
        driver = self.driver

        # Accept cookies
        self.wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button"))).click()

        # Click on the account icon/button
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))).click()

        # Select the "Register" option
        register_option = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(register_option)
        register_option.click()

        # Wait for the registration page to load
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))

        # Fill in registration form
        email = "test_{}@user.com".format(int(time.time()))
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys("test**11")
        driver.find_element(By.NAME, "repeatPassword").send_keys("test**11")
        driver.find_element(By.NAME, "firstName").send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")

        # Select country
        country_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a country']]")))
        country_dropdown.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='CA']"))).click()

        # Select state
        state_dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a state']]")))
        state_dropdown.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//option[@value='QC']"))).click()

        # Click some place to avoid dropdown hiding
        driver.find_element(By.TAG_NAME, "body").click()

        # Submit the form
        driver.find_element(By.XPATH, "//button[text()='Register']").click()

        # Confirm registration success
        self.wait.until(EC.url_contains("/my-account"))
        current_url = driver.current_url
        self.assertIn("/my-account", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()