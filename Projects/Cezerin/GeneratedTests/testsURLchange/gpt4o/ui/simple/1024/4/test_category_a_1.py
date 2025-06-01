import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryA1Page(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")

    def test_elements_present_and_visible(self):
        driver = self.driver

        # Define a wait with a timeout of 20 seconds
        wait = WebDriverWait(driver, 20)

        try:
            # Check Header Exists and is visible
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
            self.assertIsNotNone(header, "Header is missing or not visible.")

            # Check Logo Exists and is visible
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img[alt='logo']")))
            self.assertIsNotNone(logo, "Logo is missing or not visible.")

            # Check Navigation Bar Exists and is visible
            nav_bar = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".primary-nav")))
            self.assertIsNotNone(nav_bar, "Navigation bar is missing or not visible.")

            # Check Search Input Exists and is visible
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
            self.assertIsNotNone(search_input, "Search input is missing or not visible.")

            # Check Breadcrumbs Exists and is visible
            breadcrumbs = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
            self.assertIsNotNone(breadcrumbs, "Breadcrumbs are missing or not visible.")

            # Check Sort Dropdown Exists and is visible
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
            self.assertIsNotNone(sort_dropdown, "Sort dropdown is missing or not visible.")

            # Check Footer Exists and is visible
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
            self.assertIsNotNone(footer, "Footer is missing or not visible.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()