import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("your-html-page-url")

    def tearDown(self):
        self.driver.quit()

    def test_filters(self):
        try:
            # Select the "Brand A" checkbox filter
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[./input[@value='Brand A']]/span"))).click()
            WebDriverWait(self.driver, 2)  # Wait for 2 seconds

            # Uncheck the "Brand A" filter
            self.driver.find_element(By.XPATH, "//label[./input[@value='Brand A']]/span").click()

            # Get initial number of visible product cards
            initial_products = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'product-caption')]"))))

            # Apply price filtering using the interactive slider component
            self.driver.find_element(By.XPATH, "//div[./input[@type='range']]").click()
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-valuenow='967.00']"))).click()

            # Get new number of visible product cards
            new_products = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//*[contains(@class, 'product-caption')]"))))

            self.assertGreater(initial_products, new_products)
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()