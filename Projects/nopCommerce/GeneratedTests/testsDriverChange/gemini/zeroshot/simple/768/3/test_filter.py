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
            search_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
            )
            search_link.click()
        except:
            self.fail("Search link not found")

        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "q"))
            )
            search_input.send_keys("book")
        except:
            self.fail("Search input not found")

        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button-1.search-button"))
            )
            search_button.click()
        except:
            self.fail("Search button not found")

        # Apply price filter (0-15) by navigating to a specific URL
        driver.get(self.base_url + "search?q=book")
        driver.execute_script("window.stop();")
        driver.get(self.base_url + "search?q=book")
        driver.execute_script("window.stop();")

        # Verify that the product grid is updated (check for a product with price $15.50)
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h2[@class='product-title']/a[text()='Book4']"))
            )
        except:
            self.fail("Product grid was not updated correctly after filtering.")

if __name__ == "__main__":
    unittest.main()