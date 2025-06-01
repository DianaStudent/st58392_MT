import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        # Check that main UI components are present: headers, buttons, links, form fields, etc.
        
        # Header
        header_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        self.assertTrue(header_element.is_displayed())
        
        # Navigation Links
        navigation_links = self.driver.find_elements(By.LINK_TEXT, "Tables")
        for link in navigation_links:
            self.assertTrue(link.is_enabled() and link.is_visible())
            
        # Buttons
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            self.assertTrue(button.is_enabled() and button.is_visible())
            
        # Form Fields
        form_fields = self.driver.find_elements(By.NAME, "username")
        for field in form_fields:
            self.assertTrue(field.is_enabled() and field.is_visible())

    def test_tables_link(self):
        # Check that tables link is present on the home page
        tables_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
        )
        self.assertTrue(tables_link.is_enabled() and tables_link.is_visible())
        
    def test_chairs_link(self):
        # Check that chairs link is present on the home page
        chairs_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Chairs"))
        )
        self.assertTrue(chairs_link.is_enabled() and chairs_link.is_visible())
        
    def test_login_link(self):
        # Check that login link is present on the home page
        login_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        self.assertTrue(login_link.is_enabled() and login_link.is_visible())
        
    def test_register_link(self):
        # Check that register link is present on the home page
        register_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
        )
        self.assertTrue(register_link.is_enabled() and register_link.is_visible())
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()