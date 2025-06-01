from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_main_ui_components(self):
        # Open the home page
        self.driver.get('http://localhost:8080/en/')

        # Check that the main UI components are present and visible on the home page
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1#store_name'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#categories > li:nth-child(1) > a'))
            )

        except:
            self.fail('Main UI components are missing or invisible on the home page')

    def test_category_pages(self):
        # Open the clothes category page
        self.driver.get('http://localhost:8080/en/3-clothes')

        # Check that the main UI components are present and visible on the clothes category page
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1#store_name'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#categories > li:nth-child(2) > a'))
            )

        except:
            self.fail('Main UI components are missing or invisible on the clothes category page')

    def test_accessories_category_page(self):
        # Open the accessories category page
        self.driver.get('http://localhost:8080/en/6-accessories')

        # Check that the main UI components are present and visible on the accessories category page
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1#store_name'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#categories > li:nth-child(3) > a'))
            )

        except:
            self.fail('Main UI components are missing or invisible on the accessories category page')

    def test_art_category_page(self):
        # Open the art category page
        self.driver.get('http://localhost:8080/en/9-art')

        # Check that the main UI components are present and visible on the art category page
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1#store_name'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#categories > li:nth-child(4) > a'))
            )

        except:
            self.fail('Main UI components are missing or invisible on the art category page')

    def test_login_page(self):
        # Open the login page
        self.driver.get('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')

        # Check that the main UI components are present and visible on the login page
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1#login_title'))
            )
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#email'))
            )

        except:
            self.fail('Main UI components are missing or invisible on the login page')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()