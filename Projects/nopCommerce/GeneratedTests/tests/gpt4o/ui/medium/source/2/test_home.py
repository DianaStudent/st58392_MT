import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        try:
            # Verify header elements
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            
            # Verify presence of links
            nav_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
            for link_text in nav_links:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
                self.assertTrue(element.is_displayed())

            # Verify search box
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
            self.assertTrue(search_box.is_displayed(), "Search box should be visible.")

            # Verify buttons
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
            )
            self.assertTrue(search_button.is_displayed(), "Search button should be visible.")

            # Interact with elements and verify UI update
            search_box.send_keys("test")
            search_button.click()

            WebDriverWait(driver, 20).until(EC.url_contains("search?q=test"))

            # Verify no error messages
            error_dialog = driver.find_elements(By.ID, "dialog-notifications-error")
            self.assertTrue(len(error_dialog) == 0 or not error_dialog[0].is_displayed(), "Error dialog should not be visible.")
        
        except Exception as e:
            self.fail(f"Test failed due to unexpected error: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()