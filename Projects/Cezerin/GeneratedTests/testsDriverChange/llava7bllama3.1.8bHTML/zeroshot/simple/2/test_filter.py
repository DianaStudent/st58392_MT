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

    def tearDown(self):
        self.driver.quit()

    def test_filters(self):
        # Go to the webpage
        self.driver.get("http://localhost:3000/category-a")

        # Wait for interactive price slider component to be clickable
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".price-filter-values")))

        # Find checkbox input element for "Brand A"
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "label[for='brand-a'] > input[type='checkbox']")))
        
        if not brand_a_checkbox:
            self.fail("Missing required element: 'Brand A' checkbox")

        # Apply filter by clicking on the checkbox
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".column.is-6-mobile")))

        # Wait for 2 seconds to ensure the filter is applied
        import time
        time.sleep(2)

        # Remove filter by unchecking the checkbox
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".column.is-6-mobile")))

        # Wait for 2 seconds to ensure the filter is removed
        time.sleep(2)

        # Find number of visible product cards before and after applying/removing filter
        initial_cards = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".column.is-6-mobile"))))
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".column.is-6-mobile")))
        time.sleep(2)
        final_cards = len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".column.is-6-mobile"))))

        # Check if the number of visible product cards has changed
        self.assertNotEqual(initial_cards, final_cards)

if __name__ == "__main__":
    unittest.main()