from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()

    def test_elements_presence_and_visibility(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Check for header and navigation links
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertTrue(header.is_displayed(), "Header is not visible")
        except:
            self.fail("Header is missing")

        try:
            nav_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav ul.nav-level-0 li a')))
            self.assertTrue(all(link.is_displayed() for link in nav_links), "Not all navigation links are visible")
        except:
            self.fail("Navigation links are missing")

        # 2. Check for the search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
        except:
            self.fail("Search input is missing")

        # 3. Check for banner presence
        try:
            banner = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.home-slider .image-gallery-image')))
            self.assertTrue(banner.is_displayed(), "Banner is not visible")
        except:
            self.fail("Banner is missing")

        # 4. Interact with the cart button
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button .icon')))
            cart_button.click()
            mini_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.mini-cart')))
            self.assertTrue(mini_cart.is_displayed(), "Mini cart did not open")
        except:
            self.fail("Cart button interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()