from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait
        
        # Open the homepage
        driver.get("http://localhost:3000")

        # Check if the logo is present and visible
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
        self.assertTrue(logo.is_displayed(), "Logo is not visible")

        # Check primary navigation links
        nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".primary-nav .nav-level-0 li .cat-parent a")))
        self.assertGreaterEqual(len(nav_links), 3, "Primary navigation links are missing or incomplete")

        # Check search input
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        self.assertTrue(search_input.is_displayed(), "Search input is not visible")

        # Check cart button
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Check banner image
        banner_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".home-slider .image-gallery-slide .image-gallery-image img")))
        self.assertTrue(banner_image.is_displayed(), "Banner image is not visible")

        # Check Best Sellers title
        best_sellers_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4.has-text-centered")))
        self.assertTrue(best_sellers_title.is_displayed(), "Best Sellers title is not visible")

        # Interact: Click on "Category A" link
        category_a_link = driver.find_element(By.LINK_TEXT, "Category A")
        category_a_link.click()

        # Verify the Category A page loaded
        current_url = driver.current_url
        self.assertIn("/category-a", current_url, "Category A page did not load after clicking the link")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()