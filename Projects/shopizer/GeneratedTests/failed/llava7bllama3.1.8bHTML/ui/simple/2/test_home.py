from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components_present(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertIsNotNone(header)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        self.assertGreater(len(buttons), 0)

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        self.assertGreater(len(links), 0)

        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, "username")))
        self.assertGreater(len(form_fields), 0)

    def test_tables_ui_components_present(self):
        self.driver.get("http://localhost/category/tables")
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertIsNotNone(header)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        self.assertGreater(len(buttons), 0)

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        self.assertGreater(len(links), 0)

    def test_chairs_ui_components_present(self):
        self.driver.get("http://localhost/category/chairs")
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
        self.assertIsNotNone(header)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "button")))
        self.assertGreater(len(buttons), 0)

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
        self.assertGreater(len(links), 0)

    def test_login_ui_components_present(self):
        self.driver.get("http://localhost/login")
        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, "username")))
        self.assertGreater(len(form_fields), 0)
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, "password")))
        self.assertGreater(len(form_fields), 0)

    def test_register_ui_components_present(self):
        self.driver.get("http://localhost/register")
        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, "username")))
        self.assertGreater(len(form_fields), 0)
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.NAME, "email")))
        self.assertGreater(len(form_fields), 0)

if __name__ == '__main__':
    unittest.main()