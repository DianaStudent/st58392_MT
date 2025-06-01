import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header navigation links
            header_links = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "header-links")))
            self.assertTrue(header_links.is_displayed(), "Header links are not visible")

            # Check for key navigation links
            home_link = driver.find_element(By.LINK_TEXT, "Home page")
            self.assertTrue(home_link.is_displayed(), "Home page link is not visible")

            search_link = driver.find_element(By.LINK_TEXT, "Search")
            self.assertTrue(search_link.is_displayed(), "Search link is not visible")

            login_link = driver.find_element(By.CLASS_NAME, "ico-login")
            self.assertTrue(login_link.is_displayed(), "Login link is not visible")
            
            # Check logo is present
            logo = driver.find_element(By.CSS_SELECTOR, "div.header-logo img")
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check search box
            search_box = driver.find_element(By.ID, "small-searchterms")
            self.assertTrue(search_box.is_displayed(), "Search box is not visible")

            # Check search button
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")

            # Check product filter by price
            price_filter = driver.find_element(By.CLASS_NAME, "product-filter.price-range-filter")
            self.assertTrue(price_filter.is_displayed(), "Price filter is not visible")

            # Interact with the search form
            search_box.send_keys("book")
            search_button.click()

            # Ensure results are displayed
            results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
            self.assertTrue(results.is_displayed(), "Search results are not visible")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

if __name__ == "__main__":
    unittest.main()