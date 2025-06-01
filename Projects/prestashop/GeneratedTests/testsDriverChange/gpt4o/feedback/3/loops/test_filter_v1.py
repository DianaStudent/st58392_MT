import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on the "Art" category in the top menu
        art_category = wait.until(
            EC.presence_of_element_located((By.XPATH, "//li[@id='category-9']/a"))
        )
        self.assertTrue(art_category, "Art category link not found.")
        art_category.click()

        # Step 3: Wait for the category page to load
        filter_section = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )
        self.assertTrue(filter_section, "Filter section not loaded.")

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        matt_paper_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox' and @id='facet_input_57074_0']/following-sibling::span"))
        )
        self.assertTrue(matt_paper_checkbox, "Matt paper filter checkbox not found.")
        # Click the corresponding label to check the checkbox
        matt_paper_checkbox.click()

        # Step 5 & 6: Wait for the filter to apply
        # Step 7: Assert that the number of product tiles is reduced from 7 to 3
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']/div[contains(@class, 'products')]/div")))
        filtered_products = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[contains(@class, 'products')]/div")
        self.assertEqual(len(filtered_products), 3, f"Expected 3 products after filtering, but found {len(filtered_products)}.")

        # Step 8: Locate and click the "Clear all" button to remove filters
        clear_all_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        )
        self.assertTrue(clear_all_button, "Clear all button not found.")
        clear_all_button.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']/div[contains(@class, 'products')]/div")))
        all_products = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[contains(@class, 'products')]/div")
        self.assertEqual(len(all_products), 7, f"Expected 7 products after clearing filters, but found {len(all_products)}.")

if __name__ == "__main__":
    unittest.main()