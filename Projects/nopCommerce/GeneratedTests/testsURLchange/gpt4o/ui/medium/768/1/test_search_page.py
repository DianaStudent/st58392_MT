import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Confirm the presence of key interface elements
        try:
            # Verify headers and navigation links
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Verify search input and button
            search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button")))

            # Verify the search form
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//form[@action='/search']")))

            # Verify product list/grid
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.products-container")))

            # Interact with the search button
            search_input.clear()
            search_input.send_keys("book")
            search_button.click()

            # Check for the presence of results
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.product-item[data-productid='1']")))

        except Exception as e:
            self.fail(f"Element not found or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()