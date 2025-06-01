import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        try:
            # Verify header links
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "Home page"))
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "New products"))
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "Search"))
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "My account"))
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "Blog"))
            self.assertTrue(self.is_element_visible(By.LINK_TEXT, "Contact us"))

            # Verify search box
            self.assertTrue(self.is_element_visible(By.ID, "small-searchterms"))

            # Verify register and login links
            self.assertTrue(self.is_element_visible(By.CLASS_NAME, "ico-register"))
            self.assertTrue(self.is_element_visible(By.CLASS_NAME, "ico-login"))

            # Verify shopping cart and wishlist
            self.assertTrue(self.is_element_visible(By.CLASS_NAME, "ico-cart"))
            self.assertTrue(self.is_element_visible(By.CLASS_NAME, "ico-wishlist"))

            # Verify slider banner
            self.assertTrue(self.is_element_visible(By.CLASS_NAME, "slider-img"))

            # Interact with search to check for UI updates
            search_box = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
            search_box.send_keys("test")
            search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
            search_button.click()

            # Verify redirected page title
            self.wait.until(EC.title_contains("Search"))

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def is_element_visible(self, by, value):
        element = self.wait.until(EC.visibility_of_element_located((by, value)))
        return element.is_displayed()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()