import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000/category-a')

    def tearDown(self):
        self.driver.quit()

    def test_presence_of_key_elements(self):
        # Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav ul li')))
        self.assertGreater(len(navigation_links), 0)

        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search-bar')))
        self.assertIsNotNone(search_bar)

        menu_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#menu-icon')))
        self.assertIsNotNone(menu_icon)

        product_list = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#product-list')))
        self.assertIsNotNone(product_list)

    def test_interaction_with_elements(self):
        # Interact with one or two elements
        button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button)))
        button.click()

        # Check that the UI updates visually after interaction
        self.assertTrue('active' in self.driver.page_source)

    def test_no_errors_after_interaction(self):
        # Verify that interactive elements do not cause errors in the UI
        try:
            button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button')))
            button.click()
        except Exception as e:
            self.fail(f'Error occurred after interaction: {e}')

if __name__ == '__main__':
    unittest.main()