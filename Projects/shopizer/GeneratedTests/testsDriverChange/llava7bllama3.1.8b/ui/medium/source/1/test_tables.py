import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_page_elements(self):
        # Navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav a"))
        )
        self.assertEqual(len(nav_links), 3)
        
        # Inputs
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search-input"))
        )
        self.assertIsNotNone(search_input)

        # Buttons
        header_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".header-button"))
        )
        self.assertIsNotNone(header_button)

    def test_tables_page_elements(self):
        self.driver.get("http://localhost/category/tables")
        
        # Table headers
        table_headers = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "table th"))
        )
        self.assertEqual(len(table_headers), 4)

    def test_chairs_page_elements(self):
        self.driver.get("http://localhost/category/chairs")
        
        # Chair images
        chair_images = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "img.product-image"))
        )
        self.assertEqual(len(chair_images), 3)

    def test_login_page_elements(self):
        self.driver.get("http://localhost/login")
        
        # Login form fields
        login_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "login-username"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "login-password"))
        )
        self.assertIsNotNone(login_input)
        self.assertIsNotNone(password_input)

    def test_register_page_elements(self):
        self.driver.get("http://localhost/register")
        
        # Register form fields
        register_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "register-username"))
        )
        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "register-password"))
        )
        self.assertIsNotNone(register_input)
        self.assertIsNotNone(password_input)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()