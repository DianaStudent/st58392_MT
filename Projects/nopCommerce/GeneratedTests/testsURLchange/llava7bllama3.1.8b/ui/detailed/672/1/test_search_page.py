import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/search')

    def test_search_page_elements(self):
        # Check if structural elements are visible
        self.assertIn("Welcome to My Website", WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1"))).text)
        self.assertIn("Home", WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//ul/li[1]/a"))).text)

        # Check presence and visibility of input fields
        search_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-bar")))
        self.assertIsNotNone(search_bar)
        advanced_search_section = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='advanced-search']")))
        self.assertIsNotNone(advanced_search_section)

        # Check presence and visibility of buttons
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.assertIsNotNone(search_button)

        # Interact with key UI elements (e.g., click button)
        search_button.click()

        # Confirm that the UI reacts visually
        self.assertIn("Search Results", WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h2"))).text)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()