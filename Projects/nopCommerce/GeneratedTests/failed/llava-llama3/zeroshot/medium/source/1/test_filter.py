from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from webdriver_manager import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class BookSearchTest(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver and navigate to the homepage
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get("http://max/")
    
    def tearDown(self):
        # Close the web browser and quit the test case
        driver.quit()
    
    def test_search_and_price_filter(self):
        # Click on the  "Search" link from the top navigation
        search_link = (By.XPATH, "//a[contains(text(),'Search')]"))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(search_link))
        self.driver.find_element(*search_link).click()
        
        # Enter the search term and perform the search
        search_box = (By.XPATH, "//input[contains(@name,'q')]/@name")
        search_value = "book"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(search_box))
        self.driver.find_element(*search_box).send_keys(search_value)
        
        # Locate and interact with the price range slider
        select = Select((By.XPATH, "//select[contains(@name,'price')]"))
        price_range = (By.XPATH, "//select[contains(@name,'price')]/option[4]")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(select))
        self.driver.find_element(*price_range).click()
        
        # Confirm success by checking that the resulting product grid is updated
        product_grid = (By.XPATH, "//table[contains(@class,'table')] tr td")
        WebDriverWait(self.driver, 20).until(EC.presence_of_elements_located(product_grid))
        if len(product_grid) == 0:
            self.fail("No product grid found.")
        
if __name__ == '__main__':
    unittest.main()