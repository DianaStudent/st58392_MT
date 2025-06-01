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
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        try:
            # Check header visibility
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Check footer visibility
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Check main navigation links
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav .cat-parent a')))
            self.assertTrue(nav_links, "Navigation links are missing")

            # Check search input field
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button .icon')))
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

            # Check that BEST SELLERS section is visible
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title.is-4')))
            self.assertTrue(best_sellers_title.is_displayed(), "BEST SELLERS section is not visible")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")
            
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()