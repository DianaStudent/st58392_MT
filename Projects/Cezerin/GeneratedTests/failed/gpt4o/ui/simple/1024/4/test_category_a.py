from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_main_ui_elements(self):
        driver = self.driver

        # Check header elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
            )
        except:
            self.fail("Header is missing.")

        # Check logo
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image"))
            )
        except:
            self.fail("Logo is missing.")

        # Check search input
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input"))
            )
        except:
            self.fail("Search input is missing.")

        # Check category links
        for category in ['Category A', 'Category B', 'Category C']:
            try:
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, category))
                )
            except:
                self.fail(f"Category link {category} is missing.")

        # Check filter button on mobile
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button.is-fullwidth"))
            )
        except:
            self.fail("Filter button is missing.")

        # Check sort dropdown
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "select"))
            )
        except:
            self.fail("Sort dropdown is missing.")

        # Check product listing
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.products"))
            )
        except:
            self.fail("Product listing is missing.")
          
        # Check footer elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
            )
        except:
            self.fail("Footer is missing.")
      
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()