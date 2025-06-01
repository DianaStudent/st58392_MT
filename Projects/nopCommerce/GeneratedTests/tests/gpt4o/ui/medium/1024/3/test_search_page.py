from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver

        # Define a wait instance with a timeout of 20 seconds
        wait = WebDriverWait(driver, 20)

        # Check presence of header links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        except:
            self.fail("Header links are missing.")

        # Check presence of search box
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search box or button is missing.")

        # Check presence of UI interactive elements, e.g., price filter
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "price-range-filter")))
            wait.until(EC.visibility_of_element_located((By.ID, "price-range-slider")))
        except:
            self.fail("Price range filter or slider is missing.")

        # Interact with an element - search button
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Verify UI updates
        try:
            wait.until(EC.url_contains("/search?q="))
        except:
            self.fail("Search action did not update the URL or UI.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()