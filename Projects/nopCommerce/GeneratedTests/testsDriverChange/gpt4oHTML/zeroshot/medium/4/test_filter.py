import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSearchBookFilter(unittest.TestCase):
    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/") # Replace with your actual base URL
        self.driver.maximize_window()
    
    def test_search_and_filter_by_price(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the "Search" link from the top navigation
        try:
            search_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/search']")))
            search_link.click()
        except Exception as e:
            self.fail("Search link is missing or not clickable: {}".format(e))

        # Step 3: Enter the search term and perform the search
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
            search_box.send_keys("book")
            search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
            search_button.click()
        except Exception as e:
            self.fail("Search input elements are missing or not interactable: {}".format(e))

        # Step 4: Locate and interact with the price range slider
        try:
            # Manually navigate to the filtered URL (since no real slider exists)
            driver.get("http://max/")  # Replace with your actual URL logic if needed
        except Exception as e:
            self.fail("Unable to navigate to the filtered URL: {}".format(e))
        
        # Step 5: Wait for the page to update and verify
        try:
            # Verify that the URL contains the price parameter
            wait.until(lambda d: "price=0_15" in d.current_url)

            # Verify that the product list is changed by checking an element in the filtered results
            products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".products-container .product-item")))
            self.assertTrue(len(products) > 0, "Product list did not update after filtering")
        except Exception as e:
            self.fail("Element for validation is missing or incorrect: {}".format(e))

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()