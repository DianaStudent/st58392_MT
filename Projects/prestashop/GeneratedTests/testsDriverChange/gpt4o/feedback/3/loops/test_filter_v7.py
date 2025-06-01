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
        if not art_category:
            self.fail("Art category link not found.")
        art_category.click()

        # Step 3: Wait for the category page to load
        filter_section = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters"))
        )
        if not filter_section:
            self.fail("Filter section not loaded.")

        # Step 4: Locate and click the "Matt paper" filter under "Composition"
        matt_paper_label = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(., 'Matt paper')]")
            )
        )
        if not matt_paper_label:
            self.fail("Matt paper filter label not found.")
        matt_paper_label.click()

        # Step 5: Wait for the filter to apply and check product count
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div")))
        filtered_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
        self.assertEqual(len(filtered_products), 3, f"Expected 3 products after filtering, but found {len(filtered_products)}.")

        # Step 6: Clear filters by reloading the page
        driver.get("http://localhost:8080/en/9-art")

        # Step 7: Wait and assert that the number of products returns to the original count - 7
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'products')]/div")))
        all_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'products')]/div")
        self.assertEqual(len(all_products), 7, f"Expected 7 products after clearing filters, but found {len(all_products)}.")

if __name__ == "__main__":
    unittest.main()