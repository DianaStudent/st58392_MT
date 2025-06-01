from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestMaxUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_load_page(self):
        self.driver.get('http://max/')
        
        # Check header presence and visibility
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
        )
        self.assertEqual(header.is_displayed(), True)

        # Check footer presence and visibility
        footer = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        self.assertEqual(footer.is_displayed(), True)

        # Check navigation links presence and visibility
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a"))
        )
        for link in nav_links:
            self.assertEqual(link.is_enabled(), True)
            self.assertEqual(link.is_displayed(), True)

        # Check form fields presence and visibility
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "form input"))
        )
        for field in form_fields:
            self.assertEqual(field.is_enabled(), True)
            self.assertEqual(field.is_displayed(), True)

    def test_login_page(self):
        self.driver.get('http://max/login?returnUrl=%2F')
        
        # Check login form presence and visibility
        login_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#loginForm"))
        )
        self.assertEqual(login_form.is_displayed(), True)

    def test_register_page(self):
        self.driver.get('http://max/register?returnUrl=%2F')
        
        # Check register form presence and visibility
        register_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#registerForm"))
        )
        self.assertEqual(register_form.is_displayed(), True)

    def test_search_page(self):
        self.driver.get('http://max/search')
        
        # Check search form presence and visibility
        search_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form#searchForm"))
        )
        self.assertEqual(search_form.is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()