import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryAUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://example.com/category-a")  # Replace with the actual URL

    def test_ui_components(self):
        driver = self.driver

        # 1. Confirm the presence of key interface elements
        try:
            # Header should be present
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            # Navigation links
            nav_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".nav-level-0 a"))
            )

            # Search input
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input"))
            )

            # Filter button on mobile
            filter_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button.is-fullwidth"))
            )

            # Product links
            product_links = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".products a"))
            )
        except:
            self.fail("One or more UI components are missing or not visible.")

        # 2. Interact with one or two elements
        try:
            # Click on the search input, input some text, and confirm the value is set
            search_input.click()
            search_input.send_keys("Test Search")
            self.assertEqual(search_input.get_attribute("value"), "Test Search")

            # Interact with a product link to ensure it navigates correctly
            product_links[0].click()

            # Verify the expected product page is opened
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-name"))
            )
        except:
            self.fail("UI interaction failed or did not update the interface as expected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()