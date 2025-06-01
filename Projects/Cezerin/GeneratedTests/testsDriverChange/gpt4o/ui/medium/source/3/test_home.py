import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify presence of main navigation links
        main_nav_links = [
            "//a[@href='/category-a']",
            "//a[@href='/category-b']",
            "//a[@href='/category-c']"
        ]
        for link in main_nav_links:
            nav_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, link)))
            if not nav_element.is_displayed():
                self.fail(f"Navigation link with href '{link}' is not visible")

        # Verify presence of search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        if not search_input.is_displayed():
            self.fail("Search input is not visible")

        # Interact with the search input
        search_input.send_keys("test")

        # Verify presence of banner
        banner = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".image-gallery")))
        if not banner.is_displayed():
            self.fail("Image banner is not visible")

        # Interact with a category link
        category_a_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
        category_a_link.click()

        # Verify UI updates by checking the new URL
        self.wait.until(EC.url_to_be("http://localhost:3000/category-a"))
        if driver.current_url != "http://localhost:3000/category-a":
            self.fail("Failed to navigate to Category A page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()