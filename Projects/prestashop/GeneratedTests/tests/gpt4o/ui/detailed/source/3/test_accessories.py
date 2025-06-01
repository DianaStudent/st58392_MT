import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)  # Wait up to 20 seconds

    def test_accessories_page_ui(self):
        driver = self.driver

        # Check if the header is visible
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible on the page.")

        # Check if the footer is visible
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible on the page.")

        # Check if the search input field is present and visible
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input field is not visible on the page.")

        # Check if the category menu is present
        try:
            categories_menu = self.wait.until(EC.visibility_of_element_located((By.ID, "top-menu")))
        except:
            self.fail("Categories menu is not visible on the page.")

        # Check if the 'Sign in' link is visible
        try:
            sign_in_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("'Sign in' link is not visible on the page.")

        # Check if product list items are present and visible
        try:
            product_list = self.wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not visible on the page.")
        
        # Click on 'Sign in' to interact and check UI reacts
        try:
            sign_in_link.click()
            self.wait.until(EC.url_contains("login"))
        except:
            self.fail("Clicking 'Sign in' did not navigate to the login page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()