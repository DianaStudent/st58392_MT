from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def test_homepage(self):
        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        self.failUnless(login_link.is_displayed())

    def test_clothes(self):
        # Navigate to clothes page
        clothes_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="http://localhost:8080/en/3-clothes"]')))
        clothes_link.click()

        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="add-to-cart"]')))
        self.failUnless(add_to_cart_button.is_displayed())

    def test_accessories(self):
        # Navigate to accessories page
        accessories_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="http://localhost:8080/en/6-accessories"]')))
        accessories_link.click()

        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="add-to-cart"]')))
        self.failUnless(add_to_cart_button.is_displayed())

    def test_art(self):
        # Navigate to art page
        art_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="http://localhost:8080/en/9-art"]')))
        art_link.click()

        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="add-to-cart"]')))
        self.failUnless(add_to_cart_button.is_displayed())

    def test_login(self):
        # Navigate to login page
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()

        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        email_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'email')))
        self.failUnless(email_field.is_displayed())

    def test_register(self):
        # Navigate to register page
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register')))
        register_link.click()

        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="header"]/div/div[1]/h1')))
        self.failUnless(header.is_displayed())
        
        first_name_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'first_name')))
        self.failUnless(first_name_field.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()