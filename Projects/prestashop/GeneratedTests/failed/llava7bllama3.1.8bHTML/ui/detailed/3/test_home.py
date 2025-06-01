from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_page_structure(self):
        # Check that the main UI components are present
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'header')), 0)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'footer')), 0)
        
        # Check that structural elements (e.g., header, footer, navigation) are visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))

    def test_input_fields_and_buttons(self):
        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertGreater(len(self.driver.find_elements(By.NAME, 'search_query')), 0)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'search_query')))
        
        self.assertGreater(len(self.driver.find_elements(By.ID, 'submit_search')), 0)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit_search')))

    def test_interact_with_key_ui_elements(self):
        # Interact with key UI elements (e.g., click buttons)
        submit_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'submit_search')))
        submit_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()