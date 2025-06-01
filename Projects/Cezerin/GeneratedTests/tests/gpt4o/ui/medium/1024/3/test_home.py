import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_home_page_ui(self):
        driver = self.driver

        # Wait for page to load and elements to be present
        wait = WebDriverWait(driver, 20)

        try:
            # Check for the header logo
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image.active img')))
            self.assertTrue(header_logo.is_displayed(), "Header logo is not displayed")

            # Check for navigation links
            nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav ul.nav-level-0 > li > div > a')
            self.assertGreaterEqual(len(nav_links), 3, "Not all navigation links are present")

            # Check for search input
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check for category link
            category_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            self.assertTrue(category_link.is_displayed(), "Category A link is not visible")
            category_link.click()

            # Wait for page to load after clicking
            wait.until(EC.url_to_be("http://localhost:3000/category-a"))

            # Go back to home page to continue verification
            driver.get("http://localhost:3000")

            # Check for the first slide image and caption
            slide_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.image-gallery-slide.center .image-gallery-image img')))
            slide_caption = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.caption-title')))

            self.assertTrue(slide_img.is_displayed(), "First slide image is not visible")
            self.assertTrue(slide_caption.is_displayed(), "Slide caption is not visible")

            # Check for the best seller product
            best_seller_product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-name')))
            self.assertTrue(best_seller_product.is_displayed(), "Best seller product is not visible")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()