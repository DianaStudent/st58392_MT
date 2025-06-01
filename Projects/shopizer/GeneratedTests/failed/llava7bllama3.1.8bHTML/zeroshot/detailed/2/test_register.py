from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TestRegistration(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost/")

    def test_register(self):
        # Click on the account icon/button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='account']"))).click()

        # Select the "Register" option
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-name='register']"))).click()

        # Wait for the registration page to load
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']")))

        # Fill in all fields: email, password, repeat password, first name, last name
        email = "test_12345@user.com"
        password = "test11"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))).send_keys(email)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))).send_keys(password)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='repeat_password']"))).send_keys(password)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='firstname']"))).send_keys("Test")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='lastname']"))).send_keys("User")

        # Select a first country from the dropdown and wait for region/state dropdown to load
        countries = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//select[@name='country_id']/option")))
        countries[0].click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-name='region-state']")))

        # Select a first state only after selecting country and click on some place, to avoid country selector hide state selector
        regions = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//select[@name='state_id']/option")))
        regions[0].click()

        # Submit the form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-name='register']"))).click()

        # Wait for the page to redirect and confirm registration success by:
        # - Checking if the URL contains "/my-account"
        current_url = self.driver.current_url
        self.assertIn("/my-account", current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()