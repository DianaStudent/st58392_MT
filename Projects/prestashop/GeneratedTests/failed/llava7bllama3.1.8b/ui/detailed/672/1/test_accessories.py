from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageStructure(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_page_structure(self):
        # Check the presence and visibility of structural elements
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//footer")))

        # Check for input fields, buttons, labels and sections
        search_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "searchbar-autocomplete")))
        product_cards = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-card']")))

        # Interact with key UI elements
        search_bar.send_keys("Test")
        search_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
        search_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()