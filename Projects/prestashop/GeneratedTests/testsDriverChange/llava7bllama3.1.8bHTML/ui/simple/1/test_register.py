from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_page_elements(self):
        # Header elements
        header_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        self.assertEqual(header_title.text, "Home")
        
        # Navigation buttons and links
        clothes_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Clothes']")))
        accessories_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Accessories']")))
        art_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='Art']")))
        
        login_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        
        # Product links
        clothes_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        accessories_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        art_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        
        # Login form elements
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "submitLogin")))
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))

        # Check if all elements are present and visible
        self.failUnless(header_title.is_displayed())
        self.failUnless(clothes_button.is_displayed())
        self.failUnless(accessories_button.is_displayed())
        self.failUnless(art_button.is_displayed())
        self.failUnless(login_link.is_displayed())
        self.failUnless(register_link.is_displayed())
        self.failUnless(clothes_link.is_displayed())
        self.failUnless(accessories_link.is_displayed())
        self.failUnless(art_link.is_displayed())
        self.failUnless(email_input.is_displayed())
        self.failUnless(password_input.is_displayed())
        self.failUnless(login_button.is_displayable())

    def test_clothes_page_elements(self):
        # Navigate to clothes page
        self.driver.get('http://localhost:8080/en/3-clothes')
        
        # Header elements
        header_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        self.assertEqual(header_title.text, "Clothes")
        
        # Product links
        product_links = self.driver.find_elements(By.XPATH, "//a[@class='product-name']")
        for link in product_links:
            self.failUnless(link.is_displayed())

    def test_accessories_page_elements(self):
        # Navigate to accessories page
        self.driver.get('http://localhost:8080/en/6-accessories')
        
        # Header elements
        header_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        self.assertEqual(header_title.text, "Accessories")
        
        # Product links
        product_links = self.driver.find_elements(By.XPATH, "//a[@class='product-name']")
        for link in product_links:
            self.failUnless(link.is_displayed())

    def test_art_page_elements(self):
        # Navigate to art page
        self.driver.get('http://localhost:8080/en/9-art')
        
        # Header elements
        header_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        self.assertEqual(header_title.text, "Art")
        
        # Product links
        product_links = self.driver.find_elements(By.XPATH, "//a[@class='product-name']")
        for link in product_links:
            self.failUnless(link.is_displayed())

    def test_login_page_elements(self):
        # Navigate to login page
        self.driver.get('http://localhost:8080/en/')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
        
        # Login form elements
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "submitLogin")))
        
        # Check if all elements are present and visible
        self.failUnless(email_input.is_displayed())
        self.failUnless(password_input.is_displayed())
        self.failUnless(login_button.is_displayable())

if __name__ == "__main__":
    unittest.main()