from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
from html_data import home, login_page, register_page, search_page
from webdriver_manager import DriverManager

class TestNiceCommerce(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(DriverManager().get_driver("chromium"))
    
    def tearDown(self):
        self.driver.quit()
    
    def test_homepage(self):
        # Load the homepage
        self.driver.get(home)
        self.assertTrue(self.is_header_visible(), 'Header is not visible on the homepage')
        self.assertTrue(self.is_footer_visible(), 'Footer is not visible on the homepage')
        self.assertTrue(self.is_navigation_visible(), 'Navigation bar is not visible on the homepage')
        
    def test_login_page(self):
        # Load the login page
        self.driver.get(login_page)
        self.assertTrue(self.is_input_fields_present(), 'Input fields are not present on the login page')
        self.assertTrue(self.is_button_present(), 'Button is missing on the login page')
        self.assertTrue(self.is_label_present(), 'Label is missing on the login page')
        self.assertTrue(self.is_section_present(), 'Section is missing on the login page')
    
    def test_register_page(self):
        # Load the register page
        self.driver.get(register_page)
        self.assertTrue(self.is_input_fields_present(), 'Input fields are not present on the register page')
        self.assertTrue(self.is_button_present(), 'Button is missing on the register page')
        self.assertTrue(self.is_label_present(), 'Label is missing on the register page')
        self.assertTrue(self.is_section_present(), 'Section is missing on the register page')
    
    def test_search_page(self):
        # Load the search page
        self.driver.get(search_page)
        self.assertTrue(self.is_input_fields_present(), 'Input fields are not present on the search page')
        self.assertTrue(self.is_button_present(), 'Button is missing on the search page')
        self.assertTrue(self.is_label_present(), 'Label is missing on the search page')
        self.assertTrue(self.is_section_present(), 'Section is missing on the search page')
    
    def is_header_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/head[1]")))
            return True
        except NoSuchElementException as e:
            return False
    
    def is_footer_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/footer[1]")))
            return True
        except NoSuchElementException as e:
            return False
    
    def is_navigation_visible(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//html/nav[1]")))
            return True
        except NoSuchElementException as e:
            return False
    
    def is_input_fields_present(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//input[contains(@type,\"text\")]")))
            return True
        except WebDriverException as e:
            return False
    
    def is_button_present(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text,'SIGN IN')]"))
            return True
        except WebDriverException as e:
            return False
    
    def is_label_present(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//label[contains(@id,\"password\")]")))
            return True
        except WebDriverException as e:
            return False
    
    def is_section_present(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'search-page')]")))
            return True
        except WebDriverException as e:
            return False

if __name__ == '__main__':
    unittest.main()