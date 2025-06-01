import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestShopReactApp(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_homepage_elements(self):
        # Test if main UI components are present on the home page
        wait = WebDriverWait(self.driver, 20)

        # Check headers exist and are visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        self.failUnless(header.is_displayed())

        # Check buttons exist and are visible
        button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button")))
        self.assertIsNotNone(button.text)
        self.failUnless(button.is_displayed())

        # Check links exist and are visible
        link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost/category/tables']")))
        self.assertIsNotNone(link.text)
        self.failUnless(link.is_displayed())

        # Check form fields exist and are visible (for login/register)
        form_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Email']")))
        self.assertIsNotNone(form_input.get_attribute('name'))
        self.failUnless(form_input.is_displayed())

    def test_tables_elements(self):
        # Test if main UI components are present on the tables page
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/category/tables")

        # Check headers exist and are visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        self.failUnless(header.is_displayed())

        # Check buttons exist and are visible
        button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button")))
        self.assertIsNotNone(button.text)
        self.failUnless(button.is_displayed())

    def test_chairs_elements(self):
        # Test if main UI components are present on the chairs page
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/category/chairs")

        # Check headers exist and are visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        self.failUnless(header.is_displayed())

    def test_login_elements(self):
        # Test if main UI components are present on the login page
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/login")

        # Check headers exist and are visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        self.failUnless(header.is_displayed())

    def test_register_elements(self):
        # Test if main UI components are present on the register page
        wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/register")

        # Check headers exist and are visible
        header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        self.failUnless(header.is_displayed())

if __name__ == "__main__":
    unittest.main()