import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccessoriesPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not visible.")

        # Verify footer
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        except:
            self.fail("Footer is not visible.")

        # Verify navigation
        try:
            navbar = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        except:
            self.fail("Navigation bar is not visible.")

        # Verify input fields and buttons
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        except:
            self.fail("Search input field is not visible.")

        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in button is not visible.")

        # Verify categories section
        try:
            categories = self.wait.until(EC.visibility_of_element_located((By.ID, "content-wrapper")))
        except:
            self.fail("Main content wrapper is not visible.")

        # Interact with UI elements (e.g., click a category)
        try:
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            accessories_link.click()
        except:
            self.fail("Failed to click Accessories link.")

        # Confirm UI reactions
        self.wait.until(EC.url_contains("6-accessories"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()