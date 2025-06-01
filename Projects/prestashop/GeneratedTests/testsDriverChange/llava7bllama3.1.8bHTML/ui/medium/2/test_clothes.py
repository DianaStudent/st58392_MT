from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/')

    def test_homepage_elements(self):
        # Confirm the presence of key interface elements
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav a')))
        self.assertGreater(len(nav_links), 0)
        
        inputs = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input')))
        self.assertGreater(len(inputs), 0)
        
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button')))
        self.assertGreater(len(buttons), 0)
        
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.banner')))
        self.assertGreater(len(banners), 0)

    def test_interactive_element(self):
        # Interact with one or two elements
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@title="Add to cart"]')))
        button.click()

        # Verify that interactive elements do not cause errors in the UI
        self.assertEqual(button.get_attribute('class'), 'cart-button')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()