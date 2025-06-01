import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible.")

        # Check footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not visible.")

        # Check for navigation elements
        nav_elements = [
            "//a[contains(text(), 'Category A')]",
            "//a[contains(text(), 'Category B')]",
            "//a[contains(text(), 'Category C')]"
        ]
        for nav in nav_elements:
            try:
                self.wait.until(EC.visibility_of_element_located((By.XPATH, nav)))
            except:
                self.fail(f"Navigation element {nav} is not visible.")

        # Check search input field
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input field is not visible.")

        # Check sort select
        try:
            sort_select = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//select")))
        except:
            self.fail("Sort select is not visible.")

        # Interact with search input
        search_input.send_keys("Test search")
        search_icon = driver.find_element(By.CLASS_NAME, 'search-icon-search')
        
        try:
            search_icon.click()
        except:
            self.fail("Search icon is not clickable.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)