import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestScenario(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_elements_present(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'header')))
        self.assertTrue(header.is_displayed())

        # Footer
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer')))
        self.assertTrue(footer.is_displayed())

        # Navigation
        navigation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'nav')))
        self.assertTrue(navigation.is_displayed())

        # Input fields, buttons, labels and sections...
        input_fields = ['email', 'password']
        for field in input_fields:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, field)))
            self.assertTrue(element.is_displayed())

        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        self.assertTrue(login_button.is_enabled())
        
        register_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Register')))
        self.assertTrue(register_link.is_displayed())

    def test_login_page_elements_present(self):
        self.driver.get('http://localhost:8080/en/login')
        # Assert login page elements...
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        password_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'password')))
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        
    def test_clothes_page_elements_present(self):
        self.driver.get('http://localhost:8080/en/3-clothes')
        # Assert clothes page elements...

if __name__ == '__main__':
    unittest.main()