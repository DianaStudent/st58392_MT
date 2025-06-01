import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://example.com')  # URL to be replaced with the actual web page URL.

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Wait for the primary header to be visible
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'header'))
            )
            self.assertIsNotNone(header, "Header not found")

            # Check presence of navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav a')
            self.assertGreater(len(nav_links), 0, "No navigation links found")

            # Check presence of search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input'))
            )
            self.assertIsNotNone(search_input, "Search input not found")

            # Check presence of a button (e.g., 'Filter products' on mobile)
            filter_button = driver.find_element(By.CSS_SELECTOR, '.button.is-fullwidth')
            self.assertTrue(filter_button.is_displayed(), "Filter button not visible")

            # Click the first navigation link and verify UI updates
            nav_links[0].click()

            # Ensure a new section, e.g., a breadcrumb navigation or category title is visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.breadcrumb'))
            )

        except Exception as e:
            self.fail(f"UI test failed due to: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()