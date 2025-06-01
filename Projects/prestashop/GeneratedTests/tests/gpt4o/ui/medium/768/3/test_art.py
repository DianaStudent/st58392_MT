import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ArtPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check for header presence
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is not present or not visible")

        # Check for presence of navigation links
        nav_links = [
            (By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        ]
        for link_selector in nav_links:
            link = self.wait.until(EC.visibility_of_element_located(link_selector))
            if not link:
                self.fail(f"Navigation link {link_selector} is not present or not visible")

        # Check for presence of login link
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        if not login_link:
            self.fail("Login link is not present or not visible")

        # Check for search bar
        search_bar = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.ui-autocomplete-input")))
        if not search_bar:
            self.fail("Search bar is not present or not visible")

        # Check for presence of a button and click it to check UI updates
        filter_button = self.wait.until(EC.visibility_of_element_located((By.ID, "search_filter_toggler")))
        if not filter_button:
            self.fail("Filter button is not present or not visible")
        
        filter_button.click()
        
        # Check if the filter section becomes visible
        filters = self.wait.until(EC.visibility_of_element_located((By.ID, "search_filters")))
        if not filters or not filters.is_displayed():
            self.fail("Filter section did not become visible after clicking the filter button")

        # Check for footer presence
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        if not footer:
            self.fail("Footer is not present or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()