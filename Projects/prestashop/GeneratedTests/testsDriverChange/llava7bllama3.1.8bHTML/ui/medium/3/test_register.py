import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_art_website(self):
        # Check presence of key interface elements
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.nav li")))
        self.assertGreater(len(nav_links), 0)
        
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_query_top")))
        self.assertEqual(search_input.get_attribute("type"), "text")

        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button.button-search")))
        self.assertEqual(submit_button.get_attribute("class"), "button button-search")

        # Interact with elements
        search_input.send_keys("test")
        submit_button.click()

        # Verify that UI updates visually
        results = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-container")))
        self.assertGreater(len(results), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()