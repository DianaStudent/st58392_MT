import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.driver.maximize_window()

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")
        
        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        
        # Check navigation links visibility
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav a')
        for link in nav_links:
            self.assertTrue(link.is_displayed(), f"Navigation link {link.text} is not visible")

        # Check search input field
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")

        # Check sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.sort select')))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown is not visible")
        
        # Check any button and interact
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.button.is-fullwidth.is-dark')))
        self.assertTrue(button.is_displayed(), "Button is not visible")
        button.click()

        # Assert the UI reacts visually (e.g., checking if a pop-up closes or appears, etc.)

    def tearDown(self):
        # Clean up and close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()