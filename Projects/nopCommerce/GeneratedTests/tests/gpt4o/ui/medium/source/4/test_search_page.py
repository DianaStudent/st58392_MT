import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPageUI(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run headless for testing
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get('http://max/search')

    def test_ui_elements(self):
        wait = WebDriverWait(self.driver, 20)

        # Verify navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            search_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
        except:
            self.fail("Navigation links are not present or not visible.")

        # Verify search input and button
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.search-box-button")))
        except:
            self.fail("Search input or search button is not present or not visible.")

        # Verify that no errors are caused by interactive elements
        # Click the search button
        search_input.send_keys("test")
        search_button.click()

        try:
            wait.until(EC.url_contains('http://max/search?q=test'))
        except:
            self.fail("UI did not update as expected after clicking the search button.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()