from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')
        self.wait = WebDriverWait(self.driver, 20)

    def test_home_page_elements(self):
        driver = self.driver

        # Check presence of logo
        logo = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        if not logo:
            self.fail("Logo is missing on the home page.")

        # Check presence of navigation links
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav ul.nav-level-0 li a')))
        if len(nav_links) < 3:
            self.fail("Not all primary navigation links are present.")

        # Check presence of search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        if not search_input:
            self.fail("Search input is missing.")

        # Check presence of cart icon
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        if not cart_icon:
            self.fail("Cart icon is missing.")

        # Check presence of the banner
        banner = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'image-gallery-image')))
        if not banner:
            self.fail("Banner is missing on the home page.")

        # Interact with the search input
        search_input.click()
        search_input.send_keys("Test Product")
        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        search_button.click()

        # Verify no errors in the UI after interaction
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'content')))
        except Exception as e:
            self.fail(f"Error in UI after searching: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()