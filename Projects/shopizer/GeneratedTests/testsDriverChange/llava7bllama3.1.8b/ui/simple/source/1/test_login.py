import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_homepage_components(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "tables")))

        # Check headers and buttons
        self.assertIn("Home", self.driver.find_elements(By.TAG_NAME, "h1")[0].text)
        
        # Check links
        link_to_tables = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "tables")))
        self.assertEqual(link_to_tables.get_attribute('href'), 'http://localhost/category/tables')

    def test_tables_page_components(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Check header
        self.assertIn("Tables", self.driver.find_elements(By.TAG_NAME, "h1")[0].text)
        
        # Check links
        link_to_home = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        self.assertEqual(link_to_home.get_attribute('href'), 'http://localhost/')
        
        link_to_chairs = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "chairs")))
        self.assertEqual(link_to_chairs.get_attribute('href'), 'http://localhost/category/chairs')

    def test_chairs_page_components(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # Check header
        self.assertIn("Chairs", self.driver.find_elements(By.TAG_NAME, "h1")[0].text)
        
        # Check links
        link_to_home = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        self.assertEqual(link_to_home.get_attribute('href'), 'http://localhost/')
        
        link_to_tables = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "tables")))
        self.assertEqual(link_to_tables.get_attribute('href'), 'http://localhost/category/tables')

    def test_login_page_components(self):
        self.driver.get("http://localhost/login")
        
        # Check header
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Login", self.driver.find_elements(By.TAG_NAME, "h1")[0].text)
        
        # Check form fields
        username_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'username')))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'password')))

    def test_register_page_components(self):
        self.driver.get("http://localhost/register")
        
        # Check header
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertIn("Register", self.driver.find_elements(By.TAG_NAME, "h1")[0].text)
        
        # Check form fields
        username_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'username')))
        password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'password')))

if __name__ == "__main__":
    unittest.main()