from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not found or not visible")

        # Check for navigation links presence
        try:
            navigation_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav ul.nav-level-0 > li > div > a")))
        except:
            self.fail("Navigation links not found or not visible")

        # Check for the search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except:
            self.fail("Search input not found or not visible")

        # Check for the cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img")))
        except:
            self.fail("Cart button not found or not visible")

        # Check for sorting dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        except:
            self.fail("Sort dropdown not found or not visible")

        # Interaction: Click on the 'Sort' dropdown and select an option
        try:
            sort_dropdown.click()
            sort_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='-date_created']")))
            sort_option.click()
        except:
            self.fail("Unable to interact with the sort dropdown")

        # Verify no errors post-interaction
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.section-footer footer")))
        except:
            self.fail("Footer not visible after interaction, indicating a possible error in the UI")

    def tearDown(self):
        # Close the WebDriver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()