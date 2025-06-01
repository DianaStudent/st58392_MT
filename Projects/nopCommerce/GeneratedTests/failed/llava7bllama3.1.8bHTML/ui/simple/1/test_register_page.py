from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max_website_elements(self):
        # Open the website
        self.driver.get('http://max/')

        # Wait for elements to be visible before checking their presence
        headers = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )
        buttons = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button"))
        )
        links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//a"))
        )
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input"))
        )

        # Check that the elements exist and are visible
        self.assertIsNotNone(headers)
        self.assertTrue(headers.is_displayed())
        self.assertIsNotNone(buttons)
        self.assertTrue(buttons.is_displayed())
        self.assertIsNotNone(links)
        self.assertTrue(links.is_displayed())
        self.assertIsNotNone(form_fields)
        self.assertTrue(form_fields.is_displayed())

    def test_login_page_elements(self):
        # Open the login page
        self.driver.get('http://max/login?returnUrl=%2F')

        # Wait for elements to be visible before checking their presence
        username_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='username']"))
        )
        password_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']"))
        )
        login_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )

        # Check that the elements exist and are visible
        self.assertIsNotNone(username_field)
        self.assertTrue(username_field.is_displayed())
        self.assertIsNotNone(password_field)
        self.assertTrue(password_field.is_displayed())
        self.assertIsNotNone(login_button)
        self.assertTrue(login_button.is_displayed())

    def test_register_page_elements(self):
        # Open the register page
        self.driver.get('http://max/register?returnUrl=%2F')

        # Wait for elements to be visible before checking their presence
        email_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='email']"))
        )
        password_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='password']")))
        register_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))

        # Check that the elements exist and are visible
        self.assertIsNotNone(email_field)
        self.assertTrue(email_field.is_displayed())
        self.assertIsNotNone(password_field)
        self.assertTrue(password_field.is_displayed())
        self.assertIsNotNone(register_button)
        self.assertTrue(register_button.is_displayed())

    def test_search_page_elements(self):
        # Open the search page
        self.driver.get('http://max/search')

        # Wait for elements to be visible before checking their presence
        search_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='search']"))
        )
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )

        # Check that the elements exist and are visible
        self.assertIsNotNone(search_input)
        self.assertTrue(search_input.is_displayed())
        self.assertIsNotNone(submit_button)
        self.assertTrue(submit_button.is_displayed())

if __name__ == '__main__':
    unittest.main()