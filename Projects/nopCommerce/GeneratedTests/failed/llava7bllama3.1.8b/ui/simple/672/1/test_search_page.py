from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_main_ui_components(self):
        try:
            # Check header section
            header_section = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertTrue(header_section.is_displayed())

            # Check search input field
            search_input_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-input")))
            self.assertTrue(search_input_field.is_displayed())
            self.assertEqual(search_input_field.get_attribute("type"), "search")

            # Check go button
            go_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='go-button']")))
            self.assertTrue(go_button.is_displayed())

            # Check search results section
            search_results_section = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-results")))
            self.assertTrue(search_results_section.is_displayed())
        except Exception as e:
            self.fail(f"Main UI components not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()