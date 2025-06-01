import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):
    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Check logo
        try:
            logo = driver.find_element(By.CLASS_NAME, 'logo-image')
            self.assertTrue(logo.is_displayed(), "Logo is not visible")
        except:
            self.fail("Logo not found or not visible")

        # Verify search input and button
        try:
            search_input = driver.find_element(By.CLASS_NAME, 'search-input')
            search_button = driver.find_element(By.CLASS_NAME, 'search-icon-search')
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
            self.assertTrue(search_button.is_displayed(), "Search button is not visible")
        except:
            self.fail("Search input or button not found or not visible")

        # Verify cart icon
        try:
            cart_button = driver.find_element(By.CLASS_NAME, 'cart-button')
            self.assertTrue(cart_button.is_displayed(), "Cart icon is not visible")
        except:
            self.fail("Cart icon not found or not visible")
        
        # Verify primary navigation
        try:
            nav = driver.find_element(By.CLASS_NAME, 'primary-nav')
            self.assertTrue(nav.is_displayed(), "Primary navigation is not visible")
        except:
            self.fail("Primary navigation not found or not visible")

        # Verify home slider
        try:
            home_slider = driver.find_element(By.CLASS_NAME, 'home-slider')
            self.assertTrue(home_slider.is_displayed(), "Home slider is not visible")
        except:
            self.fail("Home slider not found or not visible")

        # Verify best sellers section
        try:
            best_sellers = driver.find_element(By.CSS_SELECTOR, '.title.is-4.has-text-centered')
            self.assertTrue(best_sellers.is_displayed(), "Best sellers section is not visible")
        except:
            self.fail("Best sellers section not found or not visible")

        # Verify footer
        try:
            footer = driver.find_element(By.TAG_NAME, 'footer')
            self.assertTrue(footer.is_displayed(), "Footer is not visible")
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()