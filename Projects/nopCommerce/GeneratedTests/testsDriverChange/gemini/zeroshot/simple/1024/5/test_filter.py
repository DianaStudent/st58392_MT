import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.base_url)

        # Search for "book"
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "small-searchterms"))
            )
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
        except:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Verify search results are displayed
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results not found")

        # Apply price filter (0-15)
        driver.get("http://max/search?q=book")
        driver.execute_script("document.getElementsByClassName('from')[0].innerText = '0'")
        driver.execute_script("document.getElementsByClassName('to')[0].innerText = '25'")

        # Verify filter applied (check for a product within the price range)
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='prices']/span[@class='price actual-price' and contains(text(),'$15.50')]"))
            )
        except:
            self.fail("Filter was not applied correctly. Product with price $15.50 not found.")

if __name__ == "__main__":
    unittest.main()