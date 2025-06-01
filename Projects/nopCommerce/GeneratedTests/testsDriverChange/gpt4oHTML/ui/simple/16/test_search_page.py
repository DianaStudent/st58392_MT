import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestMainUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://max/"

    def test_main_ui_components(self):

        # Navigate to home page
        self.driver.get(self.base_url)

        # Verify header elements
        try:
            header_links = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-links")))
        except Exception:
            self.fail("Header links are missing or not visible.")

        # Verify register and login links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
        except Exception:
            self.fail("Register or Login links are missing or not visible.")

        # Verify search box is present
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = search_box.find_element(By.ID, "small-searchterms")
            search_button = search_box.find_element(By.CLASS_NAME, "search-box-button")
            self.assertTrue(search_input.is_displayed() and search_button.is_displayed())
        except Exception:
            self.fail("Search box or search button is missing or not visible.")

        # Navigate and verify other pages
        self.navigate_and_verify("http://max/search", "Search page")
        self.navigate_and_verify("http://max/login?returnUrl=%2F", "Login page")
        self.navigate_and_verify("http://max/register?returnUrl=%2F", "Register page")

    def navigate_and_verify(self, url, description):
        self.driver.get(url)
        try:
            body = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
            self.assertTrue(body.is_displayed(), f"{description} is not visible.")
        except Exception:
            self.fail(f"{description} is missing or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()