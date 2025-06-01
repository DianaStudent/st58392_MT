from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

    def test_main_ui_components(self):
        self.driver.get("http://localhost:8080/en/")
        
        # Check that main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-heading']")))
        self.assertTrue(header.is_displayed(), "Header is not visible")
        
        categories = self.driver.find_elements(By.XPATH, "//ul[@class='nav nav-tabs']/li/a")
        self.assertEqual(len(categories), 4, "Number of categories do not match (Expected: 4, Actual: {})".format(len(categories)))
        
        for category in categories:
            self.assertTrue(category.is_displayed(), "Category '{}' is not visible".format(category.text))
        
        # Check that login and register links are present
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='login']")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='create-account _member-info']")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()