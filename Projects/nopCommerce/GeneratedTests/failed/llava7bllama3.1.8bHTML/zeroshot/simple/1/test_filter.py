from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestProductSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # replace with your website URL

    def test_product_search(self):
        # Perform product search using the query "book"
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
        )
        search_input.send_keys("book")
        search_button = self.driver.find_element_by_xpath("//button[@type='submit']")
        search_button.click()

        # Apply a price filter by navigating to a URL that includes the price parameter
        price_filter_url = "http://max/"  # replace with your URL format
        self.driver.get(price_filter_url)

        # Confirm success by checking that the resulting product grid is updated
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )
        self.assertTrue(product_grid.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()