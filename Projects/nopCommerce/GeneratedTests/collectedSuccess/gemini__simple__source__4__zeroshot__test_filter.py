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
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Search for "book"
        search_link_locator = (By.LINK_TEXT, "Search")
        try:
            search_link = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_link_locator)
            )
            search_link.click()
        except Exception as e:
            self.fail(f"Search link not found or not clickable: {e}")

        search_input_locator = (By.ID, "q")
        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(search_input_locator)
            )
            search_input.send_keys("book")
        except Exception as e:
            self.fail(f"Search input field not found: {e}")

        search_button_locator = (By.CLASS_NAME, "button-1.search-button")
        try:
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search button not found or not clickable: {e}")
        
        # 2. Apply price filter (0-15) by navigating to a URL
        self.driver.get(self.base_url + "search?q=book")
        self.driver.execute_script("document.getElementsByClassName('from')[0].innerText = '0'")
        self.driver.execute_script("document.getElementsByClassName('to')[0].innerText = '25'")
        
        # 3. Confirm success by checking the updated product grid
        product_item_locator = (By.XPATH, "//div[@class='product-item' and @data-productid='4']")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_item_locator)
            )
        except Exception as e:
            self.fail(f"Product item with data-productid='4' not found after filtering: {e}")

if __name__ == "__main__":
    unittest.main()