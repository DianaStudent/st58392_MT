from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_verifying_UI_elements(self):
        driver = self.driver

        # Wait for and verify the title
        try:
            WebDriverWait(driver, 20).until(EC.title_contains("Your store. Search"))
        except:
            self.fail("Page title does not contain 'Your store. Search'")

        # Wait for and verify the search box
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search box is not visible")

        # Wait for and verify the search button
        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button"))
            )
        except:
            self.fail("Search button is not visible")

        # Wait for and verify advanced search checkbox
        try:
            adv_search_checkbox = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "advs"))
            )
        except:
            self.fail("Advanced search checkbox is not visible")
        
        # Verify the main navigation links
        nav_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
        for link_text in nav_links:
            try:
                WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
            except:
                self.fail(f"Navigation link '{link_text}' is not visible")

        # Verify product sorting dropdown
        try:
            sorting_dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "products-orderby"))
            )
        except:
            self.fail("Product sorting dropdown is not visible")

        # Verify product display size dropdown
        try:
            page_size_dropdown = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "products-pagesize"))
            )
        except:
            self.fail("Product display size dropdown is not visible")
        
        # Verify price range slider
        try:
            price_slider = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "price-range-slider"))
            )
        except:
            self.fail("Price range slider is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()