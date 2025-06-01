import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver
        
        # Check for logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image img[alt='logo']")))
        except Exception:
            self.fail("Logo is not present or not visible.")

        # Check for search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input[placeholder='Search']")))
        except Exception:
            self.fail("Search input is not present or not visible.")

        # Check for category links
        try:
            category_a = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            category_b = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            category_c = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        except Exception:
            self.fail("Category links are not present or not visible.")

        # Check for main image slider
        try:
            main_slider = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.image-gallery-image img[src='/assets/images/slide8.jpg']")))
        except Exception:
            self.fail("Main image slider is not present or not visible.")

        # Check for best sellers section
        try:
            best_sellers = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.title.is-4.has-text-centered")))
            self.assertEqual(best_sellers.text, "BEST SELLERS", "Best Sellers section title is incorrect.")
        except Exception:
            self.fail("Best Sellers section is not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()