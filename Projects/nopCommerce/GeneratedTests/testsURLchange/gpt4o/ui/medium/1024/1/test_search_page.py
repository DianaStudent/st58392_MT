from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for the presence of header elements
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        except TimeoutException:
            self.fail("Header is not visible")

        # Check for navigation links
        navigation_links = ["Home page", "New products", "Search", "My account", "Blog", "Contact us"]
        for link_text in navigation_links:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except TimeoutException:
                self.fail(f"Navigation link '{link_text}' is not visible")

        # Check for search input box
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        except TimeoutException:
            self.fail("Search input box is not visible")

        # Check for search button
        try:
            search_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='button-1 search-box-button']")))
        except TimeoutException:
            self.fail("Search button is not visible")

        # Interact with the search button and check if it triggers any changes
        search_box = driver.find_element(By.ID, "small-searchterms")
        search_box.send_keys("test")
        search_button.click()

        # Verify that interactive elements do not cause errors
        try:
            self.wait.until(EC.url_contains('/search'))
        except TimeoutException:
            self.fail("URL did not update after search action")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()