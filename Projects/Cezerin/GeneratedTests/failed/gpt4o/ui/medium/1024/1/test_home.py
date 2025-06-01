from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_home_page_elements(self):
        driver = self.driver
        
        try:
            # Wait for header logo
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo-image'))
            )

            # Check the primary navigation links
            primary_nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav .nav-level-0 a')
            for element in primary_nav_links:
                self.assertTrue(element.is_displayed(), "Primary navigation link is not visible")

            # Check the search input field
            search_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input'))
            )
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")
            
            # Check the cart button
            cart_button = driver.find_element(By.CSS_SELECTOR, '.cart-button')
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

            # Check the banner
            banner = driver.find_element(By.CSS_SELECTOR, '.image-gallery-slide .image-gallery-image img')
            self.assertTrue(banner.is_displayed(), "Banner image is not visible")
            
            # Interact with a category link
            category_a_link = driver.find_element(By.CSS_SELECTOR, 'a[href="/category-a"]')
            category_a_link.click()

            # Verify the new page loads
            WebDriverWait(driver, 20).until(
                EC.url_contains("/category-a")
            )
            self.assertIn("/category-a", driver.current_url, "Failed to navigate to Category A page")

        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()