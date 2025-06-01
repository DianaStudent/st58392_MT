import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Key

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        # Set up webdriver manager to manage ChromeDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser after test execution
        self.driver.quit()

    def test_registration_page(self):
        # Load the registration page
        self.driver.get("http://localhost/register")

        # Check structural elements (e.g., header, footer, navigation)
        assert "Header" in self.driver.title
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header[contains(text(), 'Registration')]")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[contains(text(), 'Register')]"))))

        # Check presence and visibility of input fields, buttons, labels, and sections
        assert "First name" in self.driver.find_element_by_name("first\_name")
        assert "Last name" in self.driver.find_element_by_name("last\_name")
        assert "Sign up" in self.driver.find_element_by_id("submit")

        # Interact with key UI elements (e.g., click buttons)
        self.driver.find_element_by_name("first\_name").send_keys("John")
        self.driver.find_element_by_name("last\_name").send_keys("Doe")
        self.driver.find_element_by_id("agree").click()
        self.driver.find_element_by_id("submit").click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Success')]")))