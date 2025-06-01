from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_shop_react_app(self):
        # Navigate to the home page
        self.driver.get("http://localhost/")

        # Wait for the main header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

        # Check that the main UI components are present on the home page
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "h1")), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 2)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "a")), 3)

        # Navigate to the tables page
        self.driver.get("http://localhost/category/tables")

        # Wait for the table header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-header")))

        # Check that the main UI components are present on the tables page
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".table-header")), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 2)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "a")), 3)

        # Navigate to the chairs page
        self.driver.get("http://localhost/category/chairs")

        # Wait for the chair header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".chair-header")))

        # Check that the main UI components are present on the chairs page
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".chair-header")), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 2)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "a")), 3)

        # Navigate to the login page
        self.driver.get("http://localhost/login")

        # Wait for the login form to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#loginForm")))

        # Check that the main UI components are present on the login page
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, "#loginForm")), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 2)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "input")), 3)

        # Navigate to the register page
        self.driver.get("http://localhost/register")

        # Wait for the register form to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#registerForm")))

        # Check that the main UI components are present on the register page
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, "#registerForm")), 1)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 2)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "input")), 3)

if __name__ == "__main__":
    unittest.main()