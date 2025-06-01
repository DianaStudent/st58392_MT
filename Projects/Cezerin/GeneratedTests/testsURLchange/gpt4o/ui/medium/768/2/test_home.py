import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the presence of the logo
        logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "logo-image")))
        self.assertTrue(logo.is_displayed())
        
        # Check navigation links
        nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.nav-level-0 > li > div > a')))
        self.assertGreater(len(nav_links), 0, "Navigation links are missing")

        # Check search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        self.assertTrue(search_input.is_displayed())

        # Check banner slider
        banner_slider = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.home-slider')))
        self.assertTrue(banner_slider.is_displayed())

        # Check product section
        products_section = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.products')))
        self.assertTrue(products_section.is_displayed())

        # Interact with a navigation link
        category_a_link = driver.find_element(By.LINK_TEXT, 'Category A')
        category_a_link.click()

        # Confirm we're on the right page
        category_a_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        self.assertTrue(category_a_heading.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()