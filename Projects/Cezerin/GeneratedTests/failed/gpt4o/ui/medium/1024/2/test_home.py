from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Verify the presence and visibility of navigation links
        for category in ['category-a', 'category-b', 'category-c']:
            nav_link = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='/{category}']")))
            self.assertTrue(nav_link.is_displayed(), f"Navigation link for {category} not visible")

        # Verify the presence and visibility of the search input
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        self.assertTrue(search_input.is_displayed(), "Search input not visible")

        # Verify the presence and visibility of the image gallery slide
        image_gallery = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "image-gallery-slide")))
        self.assertTrue(image_gallery.is_displayed(), "Image gallery slide not visible")

        # Verify the presence and visibility of the BEST SELLERS section
        best_sellers_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'BEST SELLERS')]")))
        self.assertTrue(best_sellers_title.is_displayed(), "BEST SELLERS title not visible")

        # Interact with search and verify no errors in UI
        search_input.click()
        search_input.send_keys("Product A")
        
        # Click the search icon
        search_icon = driver.find_element(By.CLASS_NAME, "search-icon-search")
        search_icon.click()
        
        # Wait for the search results to update
        WebDriverWait(driver, 5).until(EC.staleness_of(search_icon))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()