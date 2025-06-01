import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_max_home_page(self):
        # Check main UI components
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'nav > ul > li'))
        )
        self.assertGreater(len(navigation_links), 0)
        
        inputs = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'input[type="text"]'))
        )
        self.assertGreater(len(inputs), 0)

        buttons = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button[type="submit"]'))
        )
        self.assertGreater(len(buttons), 0)

        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#banner'))
        )

        # Interact with an element
        buttons[0].click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.message')))

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(navigation_links[0].is_enabled())
        self.assertTrue(inputs[0].is_enabled())
        self.assertTrue(buttons[0].is_enabled())

if __name__ == '__main__':
    unittest.main()