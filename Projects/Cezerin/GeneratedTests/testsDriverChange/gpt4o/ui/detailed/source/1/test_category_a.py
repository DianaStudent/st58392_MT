import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CategoryPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        header_present = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        if not header_present:
            self.fail("Header is not present")

        # Check footer elements
        footer_present = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        if not footer_present:
            self.fail("Footer is not present")

        # Check navigation links
        categories = ["Category A", "Category B", "Category C"]
        for category in categories:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            except:
                self.fail(f"Navigation link for {category} is not present")

        # Check search input field
        search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        if not search_box:
            self.fail("Search input field is not present")

        # Check sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "select")))
        if not sort_dropdown:
            self.fail("Sort dropdown is not present")

        # Check product links
        products = ["Product A", "Product B"]
        for product in products:
            try:
                product_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product)))
            except:
                self.fail(f"Product link for {product} is not present")

        # Interact with sort dropdown
        sort_dropdown.click()
        favorite_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[@value='stock_status,price,position']")))
        if not favorite_option:
            self.fail("Favorite sort option is not clickable")
        favorite_option.click()

        # Assert the UI reacts (as this is a dummy, we'll assume a change is visual)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()