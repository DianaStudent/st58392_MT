from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver

        # Check header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        if not header.is_displayed():
            self.fail("Header is not visible")

        # Check footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        if not footer.is_displayed():
            self.fail("Footer is not visible")

        # Check main structural elements
        navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
        if not navigation.is_displayed():
            self.fail("Navigation is not visible")

        main_content = self.wait.until(EC.visibility_of_element_located((By.ID, "main")))
        if not main_content.is_displayed():
            self.fail("Main content is not visible")

        # Check search box is present
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        if not search_box.is_displayed():
            self.fail("Search box is not visible")

        # Check buttons are present
        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        if not search_button.is_displayed():
            self.fail("Search button is not visible")

        # Ensure key UI interactions behave correctly
        self.interact_with_ui_elements()

    def interact_with_ui_elements(self):
        driver = self.driver

        # Interact with search button
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Verify that clicking search shows some reaction
        search_result = self.wait.until(EC.url_contains("/search"))
        if not search_result:
            self.fail("Search action did not work correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()