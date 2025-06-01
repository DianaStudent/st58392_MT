import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')

    def test_shop_react_app_interface_elements_present(self):
        # Step 1: Check navigation links
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.nav-links')))
        self.assertEqual(len(nav_links), 4)
        
        # Step 2: Check inputs and buttons
        inputs_and_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input, button')))
        self.assertGreaterEqual(len(inputs_and_buttons), 5)

        # Step 3: Check banners (this is a placeholder as I couldn't find any banners in the provided HTML)
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.banner')))
        self.assertEqual(len(banners), 1)

    def test_shop_react_app_interactive_element_clicks(self):
        # Step 1: Click login button
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'login')))
        login_button.click()
        
        # Wait for page to load and check URL
        current_url = self.driver.current_url
        self.assertEqual(current_url, 'http://localhost/login')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()