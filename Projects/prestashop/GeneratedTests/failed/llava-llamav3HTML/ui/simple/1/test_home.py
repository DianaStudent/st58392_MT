from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        assert driver.find_element_by_tag_name('h1')
        assert driver.find_element_by_tag_name('button')
        assert driver.find_element_by_tag_name('a')
        assert driver.find_element_by_tag_name('form')
        for field in ['username', 'password']:
            assert driver.find_element_by_name(field)
        for link in ['register', 'login']:
            assert driver.find_element_by_name(link)
        for category in ['clothes', 'accessories', 'art']:
            assert driver.find_element_by_name(category)

    def test_login(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/login")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'back')))
        back_button = driver.find_element_by_name('back')
        assert back_button.is_enabled()

    def test_register(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/registration")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'password')))
        password_field = driver.find_element_by_name('password')
        assert password_field.is_enabled()

if __name__ == '__main__':
    unittest.main()