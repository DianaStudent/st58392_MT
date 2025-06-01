import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver with WebDriver Manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_ui_elements(self):
        driver = self.driver
        
        # Open the clothes page
        driver.get("http://localhost:8080/en/3-clothes")

        try:
            # Wait for and confirm presence of navigation link "Home"
            home_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="http://localhost:8080/en/"]'))
            )
            self.assertTrue(home_link.is_displayed(), "Home link is not visible")

            # Wait for and confirm presence of language selector
            language_selector = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#_desktop_language_selector'))
            )
            self.assertTrue(language_selector.is_displayed(), "Language selector is not visible")

            # Wait for and confirm presence of search bar
            search_bar = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search our catalog"]'))
            )
            self.assertTrue(search_bar.is_displayed(), "Search bar is not visible")

            # Wait for and confirm presence of the category title
            category_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.h1'))
            )
            self.assertEqual(category_title.text, "Clothes", "Category title is not 'Clothes'")

            # Interact with 'Sign in' button and check for update
            sign_in_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[title="Log in to your customer account"]'))
            )
            sign_in_link.click()

            # Verify new page by checking the URL
            WebDriverWait(driver, 20).until(
                EC.url_contains("http://localhost:8080/en/login")
            )
            
        except Exception as e:
            self.fail(f"Test failed due to an exception: {str(e)}")

    def tearDown(self):
        # Close the browser after the test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()