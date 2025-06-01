import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page and navigate to "Art" category
        art_category = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and text()=' Art ']"))
        )
        if not art_category:
            self.fail("Art category link not found.")
        art_category.click()

        # Step 2: Wait for the category page to load
        content_wrapper = wait.until(EC.presence_of_element_located((By.ID, "content-wrapper")))
        if not content_wrapper:
            self.fail("Art category page did not load.")

        # Step 3: Locate the filter section for Composition and apply "Matt paper"
        try:
            filter_composition_matt_paper = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(., ' Matt paper ')]/input")
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

            # Step 5: Locate and click the "Clear all" link
            clear_all_link = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//section[@id='js-active-search-filters']//a[contains(text(), 'Clear all')]")
                )
            )
            clear_all_link.click()

            # Step 6: Wait and assert that the number of products returns to the original count
            product_list = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@id='js-product-list']//article")
                )
            )
            self.assertEqual(len(product_list), 7, "Product count did not return to 7 after clearing filters.")

        except Exception as e:
            self.fail(f"Failed during filter application process: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()