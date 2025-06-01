import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMainUIComponents(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_main_ui_components(self):
        self.driver.get("http://localhost/")
        
        # Check headers
        header_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        self.assertEqual(header_title.text, "Shop React App")
        
        # Check buttons
        home_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Home']")))
        tables_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Tables")))
        
        # Check links
        self.assertEqual(tables_link.get_attribute('href'), 'http://localhost/category/tables')
        
        # Check form fields
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'searchQuery')))
        
        # Check login link
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        self.assertEqual(login_link.get_attribute('href'), 'http://localhost/login')
        
        # Check register link
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        self.assertEqual(register_link.get_attribute('href'), 'http://localhost/register')

if __name__ == "__main__":
    unittest.main()