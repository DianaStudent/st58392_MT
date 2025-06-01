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
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_main_ui_components(self):
        driver = self.driver
        wait = self.wait
        
        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
        except:
            self.fail("Logo is not visible on the home page")
        
        # Check header links
        try:
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a')))
            categories = ["Category A", "Category B", "Category C"]
            for link, category in zip(nav_links, categories):
                self.assertEqual(link.text, category)
        except:
            self.fail("Header links are not present or visible")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-input")))
        except:
            self.fail("Search input is not visible")

        # Check cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart-button")))
        except:
            self.fail("Cart icon is not visible")

        # Check image slider
        try:
            slider = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "home-slider")))
        except:
            self.fail("Image slider is not visible")

        # Check best sellers section
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='BEST SELLERS']")))
        except:
            self.fail("Best sellers section is not visible or not present")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()