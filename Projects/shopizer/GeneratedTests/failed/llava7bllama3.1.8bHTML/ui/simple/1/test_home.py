from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components_present(self):
        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1")))
        self.assertGreater(len(headers), 0)
        
        # Check if the 'Tables' link is visible
        tables_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
        self.assertIsNotNone(tables_link)
        
        # Check if the 'Chairs' link is visible
        chairs_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        self.assertIsNotNone(chairs_link)

        # Check if the 'Login' and 'Register' links are visible
        login_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        register_link = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(login_link)
        self.assertIsNotNone(register_link)

    def test_tables_ui_components_present(self):
        # Navigate to the 'Tables' page
        tables_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Tables")))
        tables_link.click()

        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        tables_headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1")))
        self.assertGreater(len(tables_headers), 0)

    def test_chairs_ui_components_present(self):
        # Navigate to the 'Chairs' page
        chairs_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Chairs")))
        chairs_link.click()

        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        chairs_headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1")))
        self.assertGreater(len(chairs_headers), 0)

    def test_login_ui_components_present(self):
        # Navigate to the 'Login' page
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        login_headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1")))
        self.assertGreater(len(login_headers), 0)

    def test_register_ui_components_present(self):
        # Navigate to the 'Register' page
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        register_link.click()

        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        register_headers = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1")))
        self.assertGreater(len(register_headers), 0)

if __name__ == '__main__':
    unittest.main()