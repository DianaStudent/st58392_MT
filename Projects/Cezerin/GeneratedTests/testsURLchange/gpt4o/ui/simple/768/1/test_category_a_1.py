import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check logo
        try:
            logo = header.find_element(By.CLASS_NAME, 'logo-image')
            self.assertTrue(logo.is_displayed(), "Logo is not visible")
        except:
            self.fail("Logo is not present")

        # Check search input
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box')))
            search_input = search_box.find_element(By.CLASS_NAME, 'search-input')
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except:
            self.fail("Search input is not present")

        # Check navigation links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.nav-level-0 > li > div.cat-parent > a')))
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are visible")
        except:
            self.fail("Navigation links are not present")

        # Check breadcrumb
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb is not visible")
        except:
            self.fail("Breadcrumb is not present")

        # Check category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
            self.assertTrue(category_title.is_displayed(), "Category title is not visible")
            self.assertEqual(category_title.text, "Subcategory 1", "Category title text is incorrect")
        except:
            self.fail("Category title is not present or incorrect")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Footer is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()