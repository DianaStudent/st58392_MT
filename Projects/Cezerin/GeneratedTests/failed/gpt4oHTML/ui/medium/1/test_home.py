from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_and_interactions(self):
        driver = self.driver
        driver.get("http://example.com")  # Replace with actual URL

        # Check for presence of main navigation links
        try:
            nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .nav-level-0 > li")))
        except Exception as e:
            self.fail(f"Navigation links are not found or visible: {e}")

        # Check for presence of search box and button
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
            search_icon = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-icon-search")))
        except Exception as e:
            self.fail(f"Search input or search icon is not found or visible: {e}")

        # Check for presence of category links in the header
        try:
            category_a_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
        except Exception as e:
            self.fail(f"Category A link is not found or visible in the navigation: {e}")

        # Interacting with the category link
        try:
            category_a_link.click()
        except Exception as e:
            self.fail(f"Failed to click category A link: {e}")

        # Verify the page update after clicking category A
        try:
            subcategory_a_1_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1")))
        except Exception as e:
            self.fail(f"Subcategory 1 link is not found or visible: {e}")

        # Perform another interaction
        try:
            subcategory_a_1_link.click()
        except Exception as e:
            self.fail(f"Failed to click subcategory 1 link: {e}")

        # Confirm page change
        try:
            WebDriverWait(driver, 20).until(lambda d: d.current_url.endswith("/category-a-1"))
        except Exception as e:
            self.fail(f"Did not navigate to subcategory 1 page: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()