from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/"

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        driver = self.driver
        base_url = self.base_url

        # Open the home page
        driver.get(base_url)

        # Click on the account button and select "Register"
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-light-link']"))
        )
        register_button.click()

        # Fill in the registration form
        email_field = WebDriverWait(driver, 20).until(
            EC.element_located((By.XPATH, "//input[@id='email']"))
        )
        email_field.send_keys("test@example.com")

        password_field = WebDriverWait(driver, 20).until(
            EC.element_located((By.XPATH, "//input[@id='password']")))
        password_field.send_keys("test**11")
        driver.find_element_by_name("first_name").send_keys("Test")
        driver.find_element_by_name("last_name").send_keys("User")

        # Select a country and a region/state
        country_select = WebDriverWait(driver, 20).until(
            EC.element_located((By.XPATH, "//select[@id='country']"))
        )
        country_select.select_by_index(0)
        driver.find_element_by_id("region_state").send_keys("Test State")
        driver.find_element_by_name("city").send_keys("Test City")

        # Submit the registration form
        register_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-light-link']"))
        )
        register_button.click()

        # Wait for redirect and confirm success by checking if the current URL includes "/my-account" in the URL
        expected_url = base_url + "/my-account"
        self.assertTrue(expected_url in driver.current_url(), "Failed to redirect after registration.")

if __name__ == '__main__':
    unittest.main()