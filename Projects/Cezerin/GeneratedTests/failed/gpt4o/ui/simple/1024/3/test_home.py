from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def tearDown(self):
        self.driver.quit()

    def test_UI_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check for header
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header, "Header is missing.")

            # Check for search input
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            self.assertIsNotNone(search_input, "Search input is missing.")

            # Check for category links
            categories = ['Category A', 'Category B', 'Category C']
            for category in categories:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
                self.assertIsNotNone(link, f"{category} link is missing.")

            # Check for best sellers section
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='BEST SELLERS']")))
            self.assertIsNotNone(best_sellers_title, "Best Sellers title is missing.")

            # Check for product name and price
            product_A_name = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='Product A']")))
            self.assertIsNotNone(product_A_name, "Product A name is missing.")

            product_A_price = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[text()='$950.00']")))
            self.assertIsNotNone(product_A_price, "Product A price is missing.")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

if __name__ == "__main__":
    unittest.main()