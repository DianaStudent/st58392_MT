import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the header is present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//h1')))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, '//h1'))

        # Check that the buttons are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@id="add-to-cart"]')))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, '//button[@id="add-to-cart"]'))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[@class="btn btn-primary"]')))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]'))

        # Check that the links are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/en/3-clothes"]')))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, '//a[@href="/en/3-clothes"]'))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[@href="/en/6-accessories"]')))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, '//a[@href="/en/6-accessories"]'))

        # Check that the form fields are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        self.assertIsNotNone(self.driver.find_element(By.NAME, 'email'))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
        self.assertIsNotNone(self.driver.find_element(By.NAME, 'password'))

    def test_clothes_link(self):
        # Click on the clothes link
        clothes_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/3-clothes"]')))
        clothes_link.click()

        # Check that we are on the clothes page
        self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/3-clothes')

    def test_accessories_link(self):
        # Click on the accessories link
        accessories_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/6-accessories"]')))
        accessories_link.click()

        # Check that we are on the accessories page
        self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/6-accessories')

    def test_art_link(self):
        # Click on the art link
        art_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/9-art"]')))
        art_link.click()

        # Check that we are on the art page
        self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/9-art')

    def test_login_link(self):
        # Click on the login link
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"]')))
        login_link.click()

        # Check that we are on the login page
        self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/login')

    def test_register_link(self):
        # Click on the register link
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/en/registration"]')))
        register_link.click()

        # Check that we are on the registration page
        self.assertEqual(self.driver.current_url, 'http://localhost:8080/en/registration')

if __name__ == '__main__':
    unittest.main()