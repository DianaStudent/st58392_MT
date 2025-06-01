import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class TestRegistration(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def test_registration(self):
        # Open the home page
        self.driver.get("http://localhost/")

        # Click on the account button and select "Register"
        account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']")))
        account_button.click()
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Fill in the registration form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'first-name')))
        first_name_input.send_keys("Test")
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'last-name')))
        last_name_input.send_keys("User")

        # Select a country and a region/state
        country_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='country']")))
        country_select.click()
        country_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//option[1]")))
        country_option.click()

        # Submit the registration form
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Wait for redirect and confirm success by checking if the current URL includes "/my-account"
        self.assertIn("/my-account", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()