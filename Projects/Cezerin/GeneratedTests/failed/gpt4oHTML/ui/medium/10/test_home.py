from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # replace with actual URL
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not present or not visible")

        # Verify the navigation links
        nav_links = [
            "/category-a",
            "/category-b",
            "/category-c"
        ]

        for link in nav_links:
            try:
                nav_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"a[href='{link}']")))
            except:
                self.fail(f"Navigation link for '{link}' is not present or not visible")

        # Verify the search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except:
            self.fail("Search input is not present or not visible")

        # Interact with the search button
        try:
            search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "img.search-icon-search")))
            search_button.click()
            # Assuming this results in visible UI change; verify it
            updated_ui = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box")))
        except:
            self.fail("Search button click did not cause expected UI interaction")

        # Verify presence of the banner (slider images)
        try:
            slider_banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".home-slider")))
        except:
            self.fail("Slider banner is not present or not visible")

        # Verify footer contact information
        footer_info = [
            "104 N Stagecoach Rd",
            "Dover Foxcroft, ME, 04426",
            "(207) 564-8482",
            "sales@shop.com"
        ]

        for info in footer_info:
            try:
                footer_element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{info}')]")))
            except:
                self.fail(f"Footer information '{info}' is not present or not visible")

        # Check that there are no visible UI errors after interactions
        try:
            self.assertFalse(driver.find_elements(By.XPATH, "//*[contains(text(), 'Error')]"), "UI contains error messages")
        except:
            self.fail("UI contains error messages")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()