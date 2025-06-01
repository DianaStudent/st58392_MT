import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_present(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#top-nav > ul > li')))
        self.assertGreater(len(navigation_links), 0)

        # Search field
        search_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'search')))
        self.assertIsNotNone(search_field)

        # Buttons and links in banner
        banner_elements = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#banner > .btn, #banner > a')))
        self.assertGreater(len(banner_elements), 0)

    def test_ui_interactions(self):
        # Click button and check UI updates
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn')))
        button.click()
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#success-message'))))

if __name__ == '__main__':
    unittest.main()