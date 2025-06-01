import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_ui_components_presence(self):
        """Test for the presence of key UI components in the search page."""

        # Navigate to the search page
        self.driver.get("http://max/search")
        
        # Check for the presence of the input field with ID 'small-searchterms'
        try:
            search_box = self.wait.until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
        except Exception as e:
            self.fail("Search box not found or not visible: " + str(e))
        
        # Check for the presence of the search button by its class 'search-box-button'
        try:
            search_button = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
        except Exception as e:
            self.fail("Search button not found or not visible: " + str(e))
        
        # Check for the presence of the navigation menu
        try:
            navigation_menu = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "top-menu"))
            )
        except Exception as e:
            self.fail("Navigation menu not found or not visible: " + str(e))
        
        # Check for the presence of the account link using href
        try:
            account_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/customer/info']"))
            )
        except Exception as e:
            self.fail("Account link not found or not visible: " + str(e))
        
        # Check for the presence of the product list using class 'products-wrapper'
        try:
            products_wrapper = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "products-wrapper"))
            )
        except Exception as e:
            self.fail("Products wrapper not found or not visible: " + str(e))
        
        # Check for the presence of a footer
        try:
            footer = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
            )
        except Exception as e:
            self.fail("Footer not found or not visible: " + str(e))

        # Check for the presence of the advanced search toggle
        try:
            adv_search_toggle = self.wait.until(
                EC.visibility_of_element_located((By.ID, "advs"))
            )
        except Exception as e:
            self.fail("Advanced search toggle not found or not visible: " + str(e))

if __name__ == "__main__":
    unittest.main()