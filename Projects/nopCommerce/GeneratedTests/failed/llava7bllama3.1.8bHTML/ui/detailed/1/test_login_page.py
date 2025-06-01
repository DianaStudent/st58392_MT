from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_max_website_structure(self):
        # Visit the website
        self.driver.get("http://max/")

        # Wait for page to load and verify that main elements are present
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-form")))
        except TimeoutException:
            self.fail("Main UI elements are not present.")

        # Check input fields, buttons, labels and sections
        try:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-input"))).is_enabled())
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-button"))).is_enabled())
        except TimeoutException:
            self.fail("Input field or button is not enabled.")

        # Interact with key UI elements and confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-button"))).click()

    def test_max_website_login_register_search(self):
        # Visit different pages
        self.driver.get("http://max/login?returnUrl=%2F")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-form")))
        
        self.driver.get("http://max/register?returnUrl=%2F")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-form")))
        
        self.driver.get("http://max/search")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search-form")))

        # Check that required UI elements exist and are visible
        try:
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "login-email"))).is_enabled())
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-button"))).is_enabled())
            self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-input"))).is_enabled())
        except TimeoutException:
            self.fail("Required UI element is missing.")

if __name__ == "__main__":
    unittest.main()