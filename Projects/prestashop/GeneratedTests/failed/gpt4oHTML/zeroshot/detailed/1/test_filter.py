from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class FilterTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_filter_matt_paper(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        homepage_url = "http://localhost:8080/en/"
        driver.get(homepage_url)
        
        # Step 2: Click on the "Art" category in the top menu
        art_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/9-art')]")))
        art_category.click()
        
        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.ID, "category")))
        
        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_facet = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[contains(@class, 'facet') and .//p[contains(text(), 'Composition')]]")))
        matt_paper_checkbox = composition_facet.find_element(By.XPATH, ".//label[contains(., 'Matt paper')]//input[@type='checkbox']")
        matt_paper_checkbox.click()

        # Step 5: Wait for the filter to apply and assert the number of product tiles is reduced from 7 to 3
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        products = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        if not products or len(products) != 3:
            self.fail(f"Expected 3 products, but found {len(products)}.")

        # Step 6: Locate and click the "Clear all" button to remove filters
        # Assuming there is a "Clear all" button found in the filter section with appropriate conditions
        clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'clear-all')]")))
        clear_all_button.click()
        
        # Step 7: Wait and assert that the number of products returns to the original count - 7
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product")))
        products_after_clear = driver.find_elements(By.CSS_SELECTOR, ".js-product")
        if not products_after_clear or len(products_after_clear) != 7:
            self.fail(f"Expected 7 products after clearing filters, but found {len(products_after_clear)}.")

if __name__ == "__main__":
    unittest.main()