import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header logo is visible
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image img')))
        except:
            self.fail("Logo not visible")

        # Verify navigation links are visible
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'ul.nav-level-0 li a')))
        except:
            self.fail("Navigation links not visible")

        # Verify search input is visible
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
        except:
            self.fail("Search input not visible")

        # Verify sort dropdown is visible
        try:
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        except:
            self.fail("Sort dropdown not visible")

        # Verify button is clickable and perform click operation
        try:
            filter_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.is-fullwidth')))
            filter_button.click()
        except:
            self.fail("Filter button not clickable or there's an error during click operation")

        # Check if mini cart is visible
        try:
            mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.mini-cart')))
        except:
            self.fail("Mini cart not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()