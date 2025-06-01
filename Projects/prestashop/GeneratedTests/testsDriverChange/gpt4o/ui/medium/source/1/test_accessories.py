import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AccessoriesPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify the presence of key interface elements
        # Header
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except:
            self.fail("Header is not present or not visible")

        # Navigation links
        nav_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Clothes"),
            (By.LINK_TEXT, "Accessories"),
            (By.LINK_TEXT, "Art"),
        ]

        for locator in nav_links:
            try:
                element = wait.until(EC.visibility_of_element_located(locator))
            except:
                self.fail(f"Navigation link for {locator} is not present or not visible")

        # Buttons
        try:
            sign_in_button = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        except:
            self.fail("Sign in button is not present or not visible")

        # Search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@aria-label='Search']")))
        except:
            self.fail("Search input is not present or not visible")

        # Banner
        try:
            banner = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-banner")))
        except:
            self.fail("Banner is not present or not visible")

        # Interact with a button
        try:
            sign_in_button.click()
            wait.until(EC.url_contains("login"))
        except:
            self.fail("Failed to interact with 'Sign in' button or URL didn't update")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()