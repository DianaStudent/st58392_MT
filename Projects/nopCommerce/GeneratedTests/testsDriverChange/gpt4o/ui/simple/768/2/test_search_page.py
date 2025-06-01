import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-text")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Header elements are not present or visible")

        # Check menu links
        menu_links = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]

        for link in menu_links:
            try:
                wait.until(EC.visibility_of_element_located(link))
            except:
                self.fail(f"Menu link '{link[1]}' is not present or visible")

        # Check search components
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "q")))
            wait.until(EC.visibility_of_element_located((By.ID, "advs")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-button")))
        except:
            self.fail("Search components are not present or visible")

        # Check product list components
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-container")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        except:
            self.fail("Product list components are not present or visible")

        # Check footer elements
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-upper")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-lower")))
        except:
            self.fail("Footer elements are not present or visible")

if __name__ == "__main__":
    unittest.main()