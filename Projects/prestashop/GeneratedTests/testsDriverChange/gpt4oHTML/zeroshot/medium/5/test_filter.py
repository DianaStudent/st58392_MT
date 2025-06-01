import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_filter_by_composition(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")
        
        # Verify page is loaded by checking existence of top menu
        top_menu = driver.find_elements(By.ID, "top-menu")
        if not top_menu:
            self.fail("Top menu not found on the home page")

        # Step 2: Navigate to the Art category
        art_category_link = driver.find_element(By.XPATH, "//a[text()=' Art ']")
        art_category_link.click()

        # Step 3: Wait for the filter sidebar to be present
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "search_filters")))
        except:
            self.fail("Filter sidebar not found on the category page")

        # Step 4: Select the 'Composition' filter for 'Matt paper'
        try:
            composition_label = driver.find_element(By.XPATH, "//section[@data-name='Composition']//label[contains(., 'Matt paper')]")
            composition_label.click()
        except:
            self.fail("Composition label for 'Matt paper' not found")

        # Step 5: Wait for the page to update and verify the number of products is reduced
        initial_products_count = len(driver.find_elements(By.XPATH, "//div[@class='js-product']"))
        
        WebDriverWait(driver, 20).until(
            lambda d: len(d.find_elements(By.XPATH, "//div[@class='js-product']")) < initial_products_count
        )
        
        filtered_products_count = len(driver.find_elements(By.XPATH, "//div[@class='js-product']"))
        if filtered_products_count >= initial_products_count:
            self.fail("The number of products did not decrease after applying the filter")

        # Step 6: Click on "Clear all" button to remove the filter
        # Assuming there is an element/button to clear all filters; this is not in provided HTML.
        # For demonstration, use the actual way to remove the filter (Clicking on same filter label).
        try:
            composition_label.click()
        except:
            self.fail("Failed to click on 'Matt paper' filter to clear it")

        # Step 7: Verify that the number of products returns to the original count
        WebDriverWait(driver, 20).until(
            lambda d: len(d.find_elements(By.XPATH, "//div[@class='js-product']")) == initial_products_count
        )
        
        restored_products_count = len(driver.find_elements(By.XPATH, "//div[@class='js-product']"))
        
        if restored_products_count != initial_products_count:
            self.fail("The number of products did not return to its original count after clearing the filter")

# Run tests
if __name__ == "__main__":
    unittest.main()