from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check for navigation links
        nav_links = [
            (By.LINK_TEXT, 'Home page'),
            (By.LINK_TEXT, 'New products'),
            (By.LINK_TEXT, 'Search'),
            (By.LINK_TEXT, 'My account'),
            (By.LINK_TEXT, 'Blog'),
            (By.LINK_TEXT, 'Contact us'),
        ]

        for by, value in nav_links:
            try:
                element = wait.until(EC.visibility_of_element_located((by, value)))
                assert element.is_displayed()
            except Exception:
                self.fail(f"Navigation link '{value}' is not displayed.")

        # Check for form inputs and buttons
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
            assert search_input.is_displayed()

            search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.search-box-button')))
            assert search_button.is_displayed()
        except Exception:
            self.fail("Search input or button is not displayed.")

        # Check for banner presence
        try:
            banner_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.slider-img')))
            assert banner_img.is_displayed()
        except Exception:
            self.fail("Banner image is not displayed.")

        # Interact with search box
        try:
            search_input.send_keys("test product")
            search_button.click()
            # Wait for page update or result
            wait.until(EC.url_changes("http://max/search?q=test+product"))
        except Exception:
            self.fail("Search interaction failed or did not lead to the expected result.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()