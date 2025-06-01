from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_main_ui_components(self):
        driver = self.driver

        try:
            # Check that main components are present on the accessories page

            # Header
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "header"))
            )

            # Main menu links
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )

            # Product List
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".products.row"))
            )

            # Search bar
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "search_widget"))
            )

            # Footer
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )

            # Subcategories
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "subcategories"))
            )

            # Product filters
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "search_filters"))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing or invisible element: {e}")

if __name__ == '__main__':
    unittest.main()