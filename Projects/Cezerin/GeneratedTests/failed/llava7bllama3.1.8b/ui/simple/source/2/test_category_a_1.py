from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')

    def test_ui_components(self):
        # Header Section
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        header = self.driver.find_element(By.TAG_NAME, 'header')
        self.failUnless(header.is_displayed(), "Header is not visible")

        # Navigation Menu
        navigation_menu_items = ['Home', 'Shop', 'Today’s Deals']
        for item in navigation_menu_items:
            link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, item)))
            self.failUnless(link.is_displayed(), f"{item} is not visible")

        # Search Field
        search_field = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'search')))
        self.failUnless(search_field.is_displayed(), "Search field is not visible")

        # Main Content Section
        main_content_section = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'main')))
        self.failUnless(main_content_section.is_displayed(), "Main content section is not visible")

        # Footer Section
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))
        self.failUnless(footer.is_displayed(), "Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()