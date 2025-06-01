from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://your-testing-url.com")  # Replace with the actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not present or visible.")

        # Check navigation links presence and visibility
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            category_a_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            subcategory_1_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))
        except:
            self.fail("Navigation links are not present or visible.")

        # Check search bar presence
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except:
            self.fail("Search input is not present or visible.")

        # Check logo presence
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@class='logo-image active']/img")))
        except:
            self.fail("Logo is not present or visible.")

        # Check category title presence
        try:
            category_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
        except:
            self.fail("Category title is not present or visible.")

        # Check filter button presence
        try:
            filter_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Filter products']")))
        except:
            self.fail("Filter button is not present or visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()