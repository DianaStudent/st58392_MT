from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up Chrome driver with webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the presence of navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
            category_b_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-b']")))
            category_c_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-c']")))
        except:
            self.fail("Navigation links are not present or visible.")

        # Check for presence of search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@class='search-input']")))
        except:
            self.fail("Search input is not present or visible.")

        # Check for presence of the sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@class, 'select')]")))
        except:
            self.fail("Sort dropdown is not present or visible.")

        # Check for presence of the filter products button
        try:
            filter_products_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Filter products']")))
        except:
            self.fail("Filter products button is not present or visible.")

        # Interact with the sort dropdown
        try:
            sort_dropdown.click()
            favorite_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='stock_status,price,position']")))
            favorite_option.click()
        except:
            self.fail("Failed to interact with the sort dropdown.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()