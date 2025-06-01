import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page and navigate to "Art" category
        art_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()='Art']"))
        )
        art_category.click()

        # Step 2: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.ID, "content-wrapper")))

        # Step 3: Locate the filter section for Composition and apply "Matt paper"
        filter_composition_matt_paper = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//label[@class='facet-label'][.//a[text()=' Matt paper ']]")
            )
        )
        filter_composition_matt_paper.click()

        # Step 4: Wait for the filter to apply and assert product count changes
        product_list = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@id='js-product-list']//article")
            )
        )
        self.assertEqual(len(product_list), 3, "Product count did not reduce to 3 after filter applied.")

        # Step 5: Locate and click the "Clear all" button
        clear_all_button = wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[@class='btn btn-secondary ok']")
            )
        )
        clear_all_button.click()

        # Step 6: Wait for removal of filters and check product count returns to 7
        product_list = wait.until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@id='js-product-list']//article")
            )
        )
        self.assertEqual(len(product_list), 7, "Product count did not return to 7 after clearing filters.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()