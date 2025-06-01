from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NopCommerceUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/")

        # Check presence of header links
        for link_text in ["Register", "Log in", "Wishlist", "Shopping cart"]:
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(element.is_displayed(), f"{link_text} link not visible.")

        # Check presence of search input and button
        search_input = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
        self.assertTrue(search_input.is_displayed(), "Search input not visible.")
        self.assertTrue(search_button.is_displayed(), "Search button not visible.")

        # Check presence of banners
        banners = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "nop-slider")))
        self.assertTrue(banners.is_displayed(), "Banner slider not visible.")

        # Interact with the search button
        search_input.send_keys("test")
        search_button.click()

        # Verify the search page loads without error
        search_page = self.wait.until(EC.title_contains("Search"))
        self.assertTrue(search_page, "Search page did not load as expected.")

        # Verify interactive elements update the UI without errors
        notification_container = self.driver.find_element(By.ID, "bar-notification")
        self.assertFalse(notification_container.is_displayed(), "Notification error visible after interaction.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()