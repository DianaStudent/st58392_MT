import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestFilterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Load base URL
        driver.get("http://max/")

        # Find the search box and button
        try:
            search_box = wait.until(
                EC.presence_of_element_located((By.ID, 'small-searchterms'))
            )
            search_button = driver.find_element(By.CLASS_NAME, 'button-1.search-box-button')
        except:
            self.fail("Search box or button not found")

        # Perform product search
        search_box.send_keys("book")
        search_button.click()

        # Verify we are on search page (before filtering)
        try:
            search_input_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'search-page'))
            )
            self.assertTrue("Search" in search_input_element.text, "Not on Search page")
        except:
            self.fail("Search page not loaded")

        # Apply price filter by visiting URL directly with parameters
        driver.get("http://max/")

        # Verify updated product grid
        try:
            products_container = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, 'products-container'))
            )
            products = products_container.find_elements(By.CLASS_NAME, 'product-item')
            if not products:
                self.fail("No products found after applying price filter")
        except:
            self.fail("Failed to load product grid after filtering")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()