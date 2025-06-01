import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import webdriver_manager.chrome

class TestWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(webdriver_manager.chrome.ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_presence_of_elements(self):
        # navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a.nav-link'))
        )
        self.assertGreater(len(navigation_links), 2)

        # search bar and button
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search_query_top'))
        )
        self.assertIsNotNone(search_bar)
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.search-button'))
        )
        self.assertIsNotNone(search_button)

        # banner
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.banner-title'))
        )
        self.assertIsNotNone(banner)

    def test_interaction_with_elements(self):
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input#search_query_top'))
        )
        search_bar.send_keys('test')
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.search-button'))
        )
        search_button.click()

    def test_no_errors_on_interaction(self):
        try:
            self.test_interaction_with_elements()
        except Exception as e:
            self.fail("Error on interaction: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()