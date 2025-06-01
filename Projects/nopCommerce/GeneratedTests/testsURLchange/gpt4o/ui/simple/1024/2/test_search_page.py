import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            search_box = header.find_element(By.CLASS_NAME, "search-box")
        except:
            self.fail("Header components are not visible")

        # Verify search input and button
        try:
            search_input = search_box.find_element(By.ID, "small-searchterms")
            search_button = search_box.find_element(By.CLASS_NAME, "search-box-button")
        except:
            self.fail("Search input or button not found or visible")

        # Verify search header and label
        try:
            search_page_title = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))
            search_label = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//label[@for='q']")))
        except:
            self.fail("Search page title or label elements are not visible")

        # Verify product grid elements
        try:
            product_grid = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
            items = product_grid.find_elements(By.CLASS_NAME, "item-box")
            if not items:
                self.fail("No items found in the product grid")
        except:
            self.fail("Product grid is not visible")

        # Verify footer elements
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            footer_links = footer.find_elements(By.TAG_NAME, "a")
            if not footer_links:
                self.fail("Footer links are not visible")
        except:
            self.fail("Footer is not visible")


if __name__ == "__main__":
    unittest.main()