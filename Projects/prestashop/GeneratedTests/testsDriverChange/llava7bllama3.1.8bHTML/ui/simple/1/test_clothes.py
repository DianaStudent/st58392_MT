import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class TestMainUI(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get('http://localhost:8080/en/')

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_elements(self):
        # Check that the main UI components are present
        main_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        self.assertEqual(main_header.text, 'Home')

        categories_links = self.driver.find_elements(By.XPATH, "//ul[@class='nav nav-list']/li/a")
        for link in categories_links:
            self.assertTrue(link.is_displayed())

        clothes_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Clothes'))
        )
        self.assertEqual(clothes_link.text, 'Clothes')

        accessories_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Accessories'))
        )
        self.assertEqual(accessories_link.text, 'Accessories')

        art_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Art'))
        )
        self.assertEqual(art_link.text, 'Art')

        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'search_query_top'))
        )
        self.assertTrue(search_input.is_enabled())

        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, 'submit_search'))
        )

        login_link = self.driver.find_element(By.LINK_TEXT, 'Login')
        self.assertTrue(login_link.is_displayed())
        self.assertEqual(login_link.text, 'Login')

        register_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Register'))
        )
        self.assertEqual(register_link.text, 'Register')

if __name__ == '__main__':
    unittest.main()