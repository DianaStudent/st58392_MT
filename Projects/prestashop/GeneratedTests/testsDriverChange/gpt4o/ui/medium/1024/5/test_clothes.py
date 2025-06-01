from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestClothesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check navigation links
        nav_links = [
            (By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"),
            (By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        ]
        for nav_link in nav_links:
            element = self.wait.until(EC.visibility_of_element_located(nav_link))
            if not element.is_displayed():
                self.fail(f"Element {nav_link} is not visible.")

        # Check banners
        banner = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-banner")))
        if not banner.is_displayed():
            self.fail("Header banner is not visible.")

        # Check search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "s")))
        if not search_input.is_displayed():
            self.fail("Search input is not visible.")

        # Check login link
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes']")))
        if not login_link.is_displayed():
            self.fail("Login link is not visible.")

        # Interact with an element
        search_input.send_keys("T-shirt")
        search_input.submit()

        # Verify no errors and UI updates
        body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
        if "error" in body.text.lower():
            self.fail("UI displayed an error after interaction.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()