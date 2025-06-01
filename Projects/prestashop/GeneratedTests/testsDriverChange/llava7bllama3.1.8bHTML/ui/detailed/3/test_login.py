import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_homepage_elements(self):
        # Header elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav//ul")))

        # Links and buttons
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            self.assertIsNotNone(link.text)
        
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            self.assertIsNotNone(button.text)

    def test_clothes_page_elements(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        # Header elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        
        # Links and buttons
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            self.assertIsNotNone(link.text)
        
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            self.assertIsNotNone(button.text)

    def test_accessories_page_elements(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        # Header elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        
        # Links and buttons
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            self.assertIsNotNone(link.text)
        
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            self.assertIsNotNone(button.text)

    def test_art_page_elements(self):
        self.driver.get("http://localhost:8080/en/9-art")
        # Header elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        
        # Links and buttons
        links = self.driver.find_elements(By.TAG_NAME, 'a')
        for link in links:
            self.assertIsNotNone(link.text)
        
        buttons = self.driver.find_elements(By.TAG_NAME, 'button')
        for button in buttons:
            self.assertIsNotNone(button.text)

    def test_login_page_elements(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        # Header elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        
        # Login form elements
        username_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        self.assertIsNotNone(username_input.get_attribute('placeholder'))
        
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'passwd')))
        self.assertIsNotNone(password_input.get_attribute('placeholder'))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()