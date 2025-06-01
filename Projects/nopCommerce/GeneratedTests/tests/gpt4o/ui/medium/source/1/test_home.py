import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Check for navigation menu
            nav_elements = WebDriverWait(driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='top-menu notmobile']/li/a"))
            )
            self.assertNotEqual(len(nav_elements), 0, "Navigation links not found or not visible")

            # Check for logo
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-logo img"))
            )
            self.assertIsNotNone(logo, "Logo not found or not visible")

            # Check search box
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
            self.assertIsNotNone(search_box, "Search box not found or not visible")

            # Check search button
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button"))
            )
            self.assertIsNotNone(search_button, "Search button not found or not visible")

            # Check top cart link
            cart_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "topcartlink"))
            )
            self.assertIsNotNone(cart_link, "Cart link not found or not visible")

            # Check banner image
            banner_image = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper-slide-active img"))
            )
            self.assertIsNotNone(banner_image, "Banner image not found or not visible")

            # Interaction Example: Click Search Button
            search_button.click()

            # Verify search page URL
            WebDriverWait(driver, 20).until(
                EC.url_contains("/search")
            )
            self.assertIn("/search", driver.current_url, "Search page URL mismatch after clicking search button")

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()