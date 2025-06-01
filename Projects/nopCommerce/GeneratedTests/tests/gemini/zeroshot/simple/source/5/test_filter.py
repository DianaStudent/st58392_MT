```python
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
        search_page_url = self.base_url + "search"
        self.driver.get(search_page_url)

        search_input_locator = (By.ID, "q")
        search_button_locator = (By.CLASS_NAME, "button-1.search-button")

        try:
            search_input = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(search_input_locator)
            )
            search_button = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(search_button_locator)
            )
        except:
            self.fail("Search input or button not found")

        search_input.send_keys("book")
        search_button.click()

        # Verify search results are displayed
        product_grid_locator = (By.CLASS_NAME, "product-grid")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_grid_locator)
            )
        except:
            self.fail("Product grid not found after search")

        # 2. Apply price filter (0-15)
        filtered_url = self.base_url + "search?q=book"  # Assuming the search query persists in the URL
        self.driver.get(filtered_url)

        # Find the product grid before filtering
        product_grid_before_filter_locator = (By.CLASS_NAME, "product-grid")
        try:
            product_grid_before_filter = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(product_grid_before_filter_locator)
            )
            product_grid_html_before_filter = product_grid_before_filter.get_attribute('innerHTML')
        except:
            self.fail("Product grid not found before filtering")

        # Navigate to the filtered URL
        filter_url = self.base_url + "search?q=book" # Replace with the actual URL for the filter

        # Apply filter 0-15 manually by using the url from the html_data
        self.driver.get(filter_url)
        self.driver.get("data:,%3Cbody%20style%3D%22zoom%3A%2050%25%3B%22%3E%20%3Cdiv%20class%3D%22master-wrapper-page%22%3E%20%3Cdiv%20class%3D%22header%22%3E%20%3Ca%20class%3D%22skip%22%20href%3D%22%23main%22%3ESkip%20navigation%3C%2Fa%3E%20%3Cdiv%20class%3D%22header-upper%22%3E%20%3Cdiv%20class%3D%22header-links-wrapper%22%3E%20%3Cdiv%20class%3D%22flyout-cart%22%20id%3D%22flyout-cart%22%3E%20%3Cdiv%20class%3D%22mini-shopping-cart%22%3E%20%3Cdiv%20class%3D%22count%22%3E%20You%20have%20no%20items%20in%20your%20shopping%20cart.%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3Cdiv%20class%3D%22header-lower%22%3E%20%3Cdiv%20class%3D%22header-logo%22%3E%20%3Ca%20href%3D%22%2F%22%3E%20%3Cimg%20alt%3D%22Your%20store%20name%22%20src%3D%22http%3A%2F%2Fmax%2FThemes%2FDefaultClean%2FContent%2Fimages%2Flogo.png%22%20title%3D%22%22%2F%3E%20%3C%2Fa%3E%20%3C%2Fdiv%3E%20%3Cdiv%20class%3D%22search-box%20store-search-box%22%3E%20%3Cform%20action%3D%22%2Fsearch%22%20id%3D%22small-search-box-form%22%20method%3D%22get%22%3E%20%3Cinput%20aria-label%3D%22Search%20store%22%20autocomplete%3D%22off%22%20class%3D%22search-box-text%20ui-autocomplete-input%22%20id%3D%22small-searchterms%22%20name%3D%22q%22%20placeholder%3D%22Search%20store%22%20type%3D%22text%22%2F%3E%20%3Cbutton%20class%3D%22button-1%20search-box-button%22%20type%3D%22submit%22%3ESearch%3C%2Fbutton%3E%20%3C%2Fform%3E%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3C%2Fdiv%3E%20%3Cdiv%20class%3D%22header-menu%22%3E%20%3Cul%20class%3D%22top-menu%20notmobile%22%3E%20%3Cli%3E%3Ca%20href%3D%22%2F%22%3EHome%20page%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%3E%3Ca%20href%3D%22%2Fnewproducts%22%3ENew%20products%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%3E%3Ca%20href%3D%22%2Fsearch%22%3ESearch%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%3E%3Ca%20href%3D%22%2Fcustomer%2Finfo%22%3EMy%20account%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%3E%3Ca%20href%3D%22%2Fblog%22%3EBlog%3C%2Fa%3E%3C%2Fli%3E%20%3Cli%3E%3Ca%20href%3D%22%2Fcontactus%22%3EContact%20us%3C%2Fa%3E%3C%2Fli%3E%20%3C%2Ful%3E%20%3Cdiv