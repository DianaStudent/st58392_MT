import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        # Set up Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_category_a_page(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open Category A page
        driver.get("http://localhost:3000/category-a")

        # 1. Confirm the presence of key interface elements
        try:
            # Verify navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))

            # Verify buttons and input fields
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))

            # Verify product thumbnails
            product_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product A")))
            product_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product B")))

        except Exception as e:
            self.fail(f"UI element presence test failed: {str(e)}")

        # 2. Interact with one or two elements
        try:
            # Interact with the sort dropdown
            sort_dropdown.click()
            newest_option = wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-date_created']")))
            newest_option.click()

            # Check that interaction does not cause errors (e.g., check page title)
            self.assertIn("Category A", driver.title)

        except Exception as e:
            self.fail(f"UI interaction test failed: {str(e)}")

    def tearDown(self):
        # Tear down the WebDriver instance
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()