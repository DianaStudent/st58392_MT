import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify presence of navigation links and interaction with them
        try:
            # Header Links
            header_links = driver.find_element(By.CLASS_NAME, "header-links")
            wait.until(EC.visibility_of(header_links))

            # Verify individual links
            nav_links = [
                ("register", "/register?returnUrl=%2F"),
                ("login", "/login?returnUrl=%2F"),
                ("wishlist", "/wishlist"),
                ("cart", "/cart"),
            ]

            for link_class, link_href in nav_links:
                link = header_links.find_element(By.CLASS_NAME, f"ico-{link_class}")
                self.assertTrue(link.is_displayed())
                self.assertIn(link_href, link.get_attribute("href"))

            # Check if the search form is available
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = driver.find_element(By.ID, "small-searchterms")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")

            self.assertTrue(search_box.is_displayed())
            self.assertTrue(search_input.is_displayed())
            self.assertTrue(search_button.is_displayed())

            # Interact with search input
            search_input.send_keys("test")
            search_button.click()

            # Verify the presence of the content on Home Page
            content = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "center-1")))
            self.assertTrue(content.is_displayed())

            # Check for banners image
            slider = driver.find_element(By.CLASS_NAME, "nop-slider")
            self.assertTrue(slider.is_displayed())

            banners = slider.find_elements(By.CLASS_NAME, "slider-img")
            self.assertGreaterEqual(len(banners), 1)

            for banner in banners:
                self.assertTrue(banner.is_displayed())

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()