from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class TestSubcategoryPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run headless if desired
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost:3000/category-a-1")

    def test_page_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header not found.")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "category-title")))
            self.assertEqual(category_title.text, "Subcategory 1")
        except:
            self.fail("Category title 'Subcategory 1' not found.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except:
            self.fail("Search input not found.")

        # Check sort dropdown
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".sort .select select")))
        except:
            self.fail("Sort dropdown not found.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer not found.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()