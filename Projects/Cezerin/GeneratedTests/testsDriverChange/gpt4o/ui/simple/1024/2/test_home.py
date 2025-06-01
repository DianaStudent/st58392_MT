import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://localhost:3000"

    def test_main_ui_elements(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            # Wait for header to be visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header.container"))
            )

            # Check for the logo
            logo = driver.find_element(By.CSS_SELECTOR, "a.logo-image")
            self.assertTrue(logo.is_displayed(), "Logo is not visible.")

            # Check for navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, "ul.nav-level-0 a")
            self.assertGreater(len(nav_links), 0, "Navigation links are not visible.")

            # Check for search input
            search_box = driver.find_element(By.CSS_SELECTOR, "input.search-input")
            self.assertTrue(search_box.is_displayed(), "Search input is not visible.")

            # Check for carousel
            carousel = driver.find_element(By.CSS_SELECTOR, "div.home-slider")
            self.assertTrue(carousel.is_displayed(), "Carousel is not visible.")

            # Check for 'Best Sellers' section
            best_sellers_title = driver.find_element(By.CSS_SELECTOR, "div.title.is-4")
            self.assertTrue(best_sellers_title.is_displayed(), "'Best Sellers' title is not visible.")

            # Check for footer
            footer = driver.find_element(By.CSS_SELECTOR, "section.section-footer footer")
            self.assertTrue(footer.is_displayed(), "Footer is not visible.")
        
        except Exception as e:
            self.fail(f"Test failed due to: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()