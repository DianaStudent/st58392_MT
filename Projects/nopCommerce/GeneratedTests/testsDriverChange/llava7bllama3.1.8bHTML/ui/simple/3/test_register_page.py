import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_main_ui_components(self):
        self.driver.get("http://max/")
        
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#header")))
        self.assertIsNotNone(header)
        
        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "button.btn")))
        self.assertGreater(len(buttons), 0)
        
        # Links
        links = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.link")))
        self.assertGreater(len(links), 0)
        
        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.form-control")))
        self.assertGreater(len(form_fields), 0)
        
    def test_login_page_ui_components(self):
        self.driver.get("http://max/login?returnUrl=%2F")
        
        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.form-control")))
        self.assertGreater(len(form_fields), 0)
        
        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-login")))
        self.assertIsNotNone(buttons)
        
    def test_register_page_ui_components(self):
        self.driver.get("http://max/register?returnUrl=%2F")
        
        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.form-control")))
        self.assertGreater(len(form_fields), 0)
        
        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-register")))
        self.assertIsNotNone(buttons)
        
    def test_search_page_ui_components(self):
        self.driver.get("http://max/search")
        
        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "input.form-control")))
        self.assertGreater(len(form_fields), 0)
        
        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-search")))
        self.assertIsNotNone(buttons)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()