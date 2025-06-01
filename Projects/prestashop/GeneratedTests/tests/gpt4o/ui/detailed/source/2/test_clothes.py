import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible")

        # Verify footer is visible
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is not visible")

        # Verify navigation links are visible
        try:
            nav_links = [
                (By.LINK_TEXT, "Clothes"),
                (By.LINK_TEXT, "Accessories"),
                (By.LINK_TEXT, "Art")
            ]
            for link in nav_links:
                element = wait.until(EC.visibility_of_element_located(link))
        except:
            self.fail("Navigation link is not visible")

        # Verify input field for search is visible
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        except:
            self.fail("Search input field is not visible")

        # Verify buttons like "Sign in" are visible
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in button is not visible")

        # Verify product list is visible
        try:
            products_section = wait.until(EC.visibility_of_element_located((By.ID, "products")))
        except:
            self.fail("Products section is not visible")

        # Interact with elements if necessary (e.g., click Sign in)
        try:
            sign_in_button.click()
            wait.until(EC.url_contains("login"))
        except:
            self.fail("Failed to interact with Sign in button")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()