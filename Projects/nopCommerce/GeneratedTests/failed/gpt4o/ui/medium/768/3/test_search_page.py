from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check navigation links
        nav_links = [
            "/",
            "/newproducts",
            "/search",
            "/customer/info",
            "/blog",
            "/contactus"
        ]
        for link in nav_links:
            try:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']")))
            except:
                self.fail(f"Navigation link with href {link} not found or not visible")

        # Check inputs and buttons
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "q")))
            search_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'search-button')]")))
        except:
            self.fail("Search input or button not found or not visible")

        # Check interactive element - click search button
        search_button.click()
        try:
            wait.until(EC.url_contains("search?q="))
        except:
            self.fail("Search action did not update the URL")

        # Check product grid visibility
        try:
            products_grid = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        except:
            self.fail("Products grid not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()