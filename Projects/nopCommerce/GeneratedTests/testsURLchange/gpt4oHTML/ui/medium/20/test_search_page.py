import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UIProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_ui_elements_and_interaction(self):
        driver = self.driver

        # Verify the presence of key UI elements
        try:
            # Wait for the header to be present
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )

            # Verify navigation links
            nav_links = header.find_elements(By.TAG_NAME, "a")
            self.assertTrue(any(link.text == "Register" for link in nav_links), "Register link is missing")
            self.assertTrue(any(link.text == "Log in" for link in nav_links), "Log in link is missing")
            self.assertTrue(any(link.text == "Wishlist" for link in nav_links), "Wishlist link is missing")
            self.assertTrue(any(link.text == "Shopping cart" for link in nav_links), "Shopping cart link is missing")

            # Check search input
            search_input = driver.find_element(By.ID, "small-searchterms")
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check search button
            search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")

            # Verify advanced search toggle
            advanced_search_toggle = driver.find_element(By.ID, "advs")
            self.assertTrue(advanced_search_toggle.is_displayed(), "Advanced search toggle is not visible")

            # Interact with a search input and button
            search_input.send_keys("book")
            search_button.click()

            # Wait for the search results to appear
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "products-container"))
            )

        except Exception as e:
            self.fail(f"Test failed due to an exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()