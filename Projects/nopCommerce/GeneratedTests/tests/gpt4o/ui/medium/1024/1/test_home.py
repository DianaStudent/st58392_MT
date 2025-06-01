import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePageUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_home_page_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the page
        driver.get("http://max/")
        
        # Step 2: Confirm the presence of key interface elements

        # Check header links
        header_links = driver.find_elements(By.CSS_SELECTOR, ".header-links a")
        if not header_links:
            self.fail("Header links are not present or visible")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".top-menu.notmobile a")
        if not nav_links:
            self.fail("Navigation links are not present or visible")

        # Check search box
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        if not search_box.is_displayed():
            self.fail("Search box is not visible")

        # Check search button
        search_button = driver.find_element(By.CSS_SELECTOR, ".search-box-button")
        if not search_button.is_displayed():
            self.fail("Search button is not visible")

        # Check banners
        banners = driver.find_elements(By.CSS_SELECTOR, ".slider-img")
        if len(banners) == 0:
            self.fail("Banners are not present or visible")

        # Step 3: Interact with one or two elements
        # Search for something
        search_box.send_keys("test")
        search_button.click()

        # Verify UI updates by checking the URL change
        self.assertIn("search", driver.current_url, "Search did not lead to search page")

        # Step 4: Verify interactive elements do not cause errors in the UI
        # Check that the search results page is loaded
        try:
            result_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page.title")))
            assert result_title.is_displayed()
        except:
            self.fail("Search result page is not loaded or missing expected elements")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()