import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify navigation links
        try:
            nav_links = wait.until(EC.visibility_of_any_elements_located((By.CSS_SELECTOR, 'header .nav-level-0 a')))
            self.assertTrue(len(nav_links) > 0, "Navigation links are missing")
        except:
            self.fail("Navigation links not visible or missing")

        # Verify search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except:
            self.fail("Search input not visible or missing")

        # Verify presence of category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.category-title')))
            self.assertTrue(category_title.is_displayed(), "Category title is not visible")
        except:
            self.fail("Category title not visible or missing")

        # Click sort dropdown and select an option
        try:
            sort_select = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
            sort_select.click()
            option_price_low_to_high = wait.until(EC.visibility_of_element_located((By.XPATH, '//option[@value="price"]')))
            option_price_low_to_high.click()
        except:
            self.fail("Sort dropdown interaction failed")

        # Verify footer is present
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Footer not visible or missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()