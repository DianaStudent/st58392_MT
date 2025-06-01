import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is missing")

        # Check footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is missing")

        # Check navigation visibility
        nav = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.header-nav")))
        self.assertIsNotNone(nav, "Navigation is missing")

        # Check input fields visibility
        search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[aria-label='Search']")))
        self.assertIsNotNone(search_input, "Search input is missing")

        # Check buttons and links
        login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))
        self.assertIsNotNone(login_button, "Login button is missing")

        register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        self.assertIsNotNone(register_link, "Register link is missing")

        # Interact with quick view button
        quick_view_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.quick-view.js-quick-view")))
        quick_view_button.click()
        
        # Verify UI reacts (e.g., modal should appear)
        quick_view_modal = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-modal")))
        self.assertTrue(quick_view_modal.is_displayed(), "Quick view modal is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()