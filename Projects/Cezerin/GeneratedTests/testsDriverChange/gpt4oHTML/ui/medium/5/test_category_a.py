import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://yourwebsite.com/category-a")  # Replace with the actual URL

    def test_ui_elements(self):
        driver = self.driver

        # Wait for and check header presence
        header = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, "ul.nav-level-0 > li > div.cat-parent > a")
        self.assertGreater(len(nav_links), 0, "Navigation links are missing")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), "Navigation link is not visible")

        # Check search input field
        search_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input"))
        )
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check sort select box
        sort_select = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "select"))
        )
        self.assertTrue(sort_select.is_displayed(), "Sort select box is not visible")

        # Check filter button for mobile (can be hidden)
        filter_button = driver.find_element(By.CSS_SELECTOR, "button.button.is-fullwidth")
        self.assertTrue(filter_button.is_displayed(), "Filter button is not visible")

        # Check product listings presence
        product_list = driver.find_elements(By.CSS_SELECTOR, "div.products > div.column")
        self.assertGreater(len(product_list), 0, "No products found")

        # Interact with a category link and verify UI update
        category_link = nav_links[0]
        category_link.click()

        # Verify that clicking on a category updates the page correctly
        WebDriverWait(driver, 20).until(
            EC.url_contains("/category-a")
        )
        current_url = driver.current_url
        self.assertIn("/category-a", current_url, "URL did not update to Category A")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()