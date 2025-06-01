import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/9-art")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible.")

        # Check main sections
        try:
            main = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "main")))
        except:
            self.fail("Main content area is not visible.")
        
        # Check navigation links
        try:
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation is not visible.")
        
        # Check login link visibility
        try:
            login = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Login link is not visible.")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input is not visible.")

        # Check category links
        categories = ["Clothes", "Accessories", "Art"]
        for category in categories:
            try:
                category_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            except:
                self.fail(f"Category link '{category}' is not visible.")
        
        # Check product list
        try:
            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
        except:
            self.fail("Product list is not visible.")

        # Interact with a button (e.g., sort button)
        try:
            sort_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Sort by selection']")))
            sort_button.click()
        except:
            self.fail("Sort button is not clickable.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()