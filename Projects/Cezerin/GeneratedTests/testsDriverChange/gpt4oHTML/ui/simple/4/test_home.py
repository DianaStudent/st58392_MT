import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost")  # Update with the correct URL for testing
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check for header
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))

            # Check for search input
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))

            # Check for search button
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'img.search-icon-search')))

            # Check for navigation links in the header
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category B')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category C')))

            # Check for the first image gallery slide
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.image-gallery-slide.center img')))

            # Check for "BEST SELLERS" section
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.title.is-4.has-text-centered')))

            # Check for footer
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'section.section-footer')))

            # Navigate through categories and subcategories
            driver.find_element(By.LINK_TEXT, 'Category A').click()
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'ul.nav-level-1')))

            driver.find_element(By.LINK_TEXT, 'Subcategory 1').click()
            # You can add further checks for elements specific to this subcategory page

        except Exception as e:
            self.fail(f"An element is missing or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()