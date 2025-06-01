from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import os

class TestShopifyApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ['SELENIUM_HUB_URL'] = 'http://localhost:4444/wd/hub'
        cls.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                      desired_capabilities={'browserName': 'chrome'})
        cls.driver.maximize_window()

    def test_main_components(self):
        self.driver.get('http://localhost:8080/en/')
        
        # Check header
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1")))
        self.assertIsNotNone(header.text)
        
        # Check categories
        categories = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='nav-list']//a")))
        self.assertGreater(len(categories), 0)
        
        # Check subcategories
        category_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='subcategory-links']/a")))
        self.assertGreater(len(category_links), 0)
        
        # Check product listing
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='products list rows']//li")))
        self.assertIsNotNone(product_list)
        
        # Check cart and wishlist buttons
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Cart']")))
        wishlist_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Wishlist']")))
        self.assertIsNotNone(cart_button)
        self.assertIsNotNone(wishlist_button)

    def test_category_pages(self):
        self.driver.get('http://localhost:8080/en/3-clothes')
        
        # Check subcategories
        category_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='subcategory-links']/a")))
        self.assertGreater(len(category_links), 0)
        
        # Check product listing
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='products list rows']//li")))
        self.assertIsNotNone(product_list)

    def test_accessories_page(self):
        self.driver.get('http://localhost:8080/en/6-accessories')
        
        # Check subcategories
        category_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='subcategory-links']/a")))
        self.assertGreater(len(category_links), 0)
        
        # Check product listing
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='products list rows']//li")))
        self.assertIsNotNone(product_list)

    def test_art_page(self):
        self.driver.get('http://localhost:8080/en/9-art')
        
        # Check subcategories
        category_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='subcategory-links']/a")))
        self.assertGreater(len(category_links), 0)
        
        # Check product listing
        product_list = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='products list rows']//li")))
        self.assertIsNotNone(product_list)

    def test_login_page(self):
        self.driver.get('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')
        
        # Check form fields
        username_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
        password_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        self.assertIsNotNone(username_field)
        self.assertIsNotNone(password_field)

    def test_register_page(self):
        self.driver.get('http://localhost:8080/en/registration')
        
        # Check form fields
        username_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='username']")))
        password_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']")))
        self.assertIsNotNone(username_field)
        self.assertIsNotNone(password_field)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()