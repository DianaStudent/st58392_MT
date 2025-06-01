from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up Chrome driver
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.get("data:text/html;charset=utf-8," + html_data["html"])
        cls.wait = WebDriverWait(cls.driver, 20)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_check_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header presence and visibility
        header = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible on the page")

        # Verify navigation links presence
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav .cat-parent a')
        self.assertTrue(len(nav_links) > 0, "No navigation links found in the header")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), f"Nav link {link.text} is not visible")

        # Verify search input and button presence
        search_input = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        search_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        self.assertTrue(search_icon.is_displayed(), "Search icon is not visible")
        
        # Verify sort dropdown menu
        sort_select = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'select')))
        self.assertTrue(sort_select.is_displayed(), "Sort dropdown is not visible")

        # Verify logo presence
        logo = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'logo-image')))
        logo_img = logo.find_element(By.TAG_NAME, 'img')
        self.assertTrue(logo_img.is_displayed(), "Logo is not visible")

    def test_interact_with_navigation_and_verify(self):
        driver = self.driver
        wait = self.wait

        # Click on "Category A" in the navigation
        category_a_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Category A')))
        category_a_link.click()

        # Verify the change in page (URL has changed or content specific to Category A)
        current_url = driver.current_url
        self.assertIn("/category-a", current_url, "Clicking Category A did not navigate to the correct page")

        # Verify Subcategories are displayed
        subcategories = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.nav-level-1 .cat-parent a')))
        self.assertTrue(len(subcategories) > 0, "Subcategories for Category A are not visible")
        for subcategory in subcategories:
            self.assertTrue(subcategory.is_displayed(), f"Subcategory {subcategory.text} is not visible")

if __name__ == "__main__":
    unittest.main()