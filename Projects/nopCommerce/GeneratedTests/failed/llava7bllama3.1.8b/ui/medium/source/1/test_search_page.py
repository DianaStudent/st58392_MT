from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/search')

    def test_search_page_elements(self):
        # Wait for navigation links to be visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.XPATH, '//ul[@class="nav-links"]/li'))
        )
        self.assertGreater(len(nav_links), 0)

        # Verify presence of search input and button
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'q')))
        self.assertIsNotNone(search_input)
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
        self.assertIsNotNone(search_button)

    def test_interact_with_elements(self):
        # Click on a navigation link
        nav_links = self.driver.find_elements(By.XPATH, '//ul[@class="nav-links"]/li')
        if len(nav_links) > 0:
            nav_links[0].click()
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//h1')))
            except TimeoutException:
                self.fail('Navigation link did not lead to expected page')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()