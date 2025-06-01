import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check if the header, search input, and button are visible
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#small-searchterms")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
        except Exception as e:
            self.fail(f"UI element not found or visible: {e}")

        # Interact with a search button
        search_box = driver.find_element(By.CSS_SELECTOR, "input#small-searchterms")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.search-box-button")

        search_box.send_keys("book")
        search_button.click()

        # Verify UI updates by checking if the results page updates correctly
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.page.search-page")))
        except Exception as e:
            self.fail(f"Search results page did not load properly: {e}")

        # Check if there are any visible products
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-item")))
        except Exception as e:
            self.fail(f"No products are visible after search: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()