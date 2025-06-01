from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header > h1')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[1]//a')))
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search_query_top')))
        except Exception as e:
            self.fail(f'Error: {str(e)}')

    def test_clothes_link(self):
        # Check that the clothes link is present and clickable
        try:
            clothes_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[2]//a')))
            clothes_link.click()
            self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/3-clothes')
        except Exception as e:
            self.fail(f'Error: {str(e)}')

    def test_accessories_link(self):
        # Check that the accessories link is present and clickable
        try:
            accessories_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[3]//a')))
            accessories_link.click()
            self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/6-accessories')
        except Exception as e:
            self.fail(f'Error: {str(e)}')

    def test_art_link(self):
        # Check that the art link is present and clickable
        try:
            art_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[4]//a')))
            art_link.click()
            self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/9-art')
        except Exception as e:
            self.fail(f'Error: {str(e)}')

    def test_login_link(self):
        # Check that the login link is present and clickable
        try:
            login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[5]//a')))
            login_link.click()
            self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')
        except Exception as e:
            self.fail(f'Error: {str(e)}')

    def test_register_link(self):
        # Check that the register link is present and clickable
        try:
            register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//ul[@class="nav navbar-nav"]//li[6]//a')))
            register_link.click()
            self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/registration')
        except Exception as e:
            self.fail(f'Error: {str(e)}')

if __name__ == '__main__':
    unittest.main()