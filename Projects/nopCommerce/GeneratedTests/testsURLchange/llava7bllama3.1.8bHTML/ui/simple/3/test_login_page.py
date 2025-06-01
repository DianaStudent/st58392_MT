import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_max_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertIn('Max', self.driver.find_element(By.TAG_NAME, 'h1').text)

        # Check that buttons and links exist
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        self.driver.find_element(By.LINK_TEXT, 'Login')

        # Check that form fields exist
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'username')))
        self.driver.find_element(By.NAME, 'password')

        # Check that other elements exist
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
        self.driver.find_element(By.XPATH, '//input[@type="submit"]')
        self.driver.find_element(By.LINK_TEXT, 'Register')

    def test_login_page_components(self):
        self.driver.get('http://max/login?returnUrl=%2F')
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertIn('Login', self.driver.find_element(By.TAG_NAME, 'h1').text)

        # Check that buttons and links exist
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submit"]')))
        self.driver.find_element(By.LINK_TEXT, 'Register')

    def test_register_page_components(self):
        self.driver.get('http://max/register?returnUrl=%2F')
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertIn('Register', self.driver.find_element(By.TAG_NAME, 'h1').text)

    def test_search_page_components(self):
        self.driver.get('http://max/search')
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertIn('Search', self.driver.find_element(By.TAG_NAME, 'h1').text)

if __name__ == '__main__':
    unittest.main()