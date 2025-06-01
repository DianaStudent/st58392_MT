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
        self.driver.get('http://localhost:3000')

    def test_ui_elements(self):
        # Check header and footer presence and visibility
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//header')))
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//footer')))

        # Check category_a link presence and visibility
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'category_a')))
        
        category_a_link = self.driver.find_element(By.LINK_TEXT, 'category_a')
        category_a_link.click()

        # Check category_a_1 link presence and visibility
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'category_a_1')))
        
        category_a_1_link = self.driver.find_element(By.LINK_TEXT, 'category_a_1')
        category_a_1_link.click()

        # Check structural elements are visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//h1')))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()