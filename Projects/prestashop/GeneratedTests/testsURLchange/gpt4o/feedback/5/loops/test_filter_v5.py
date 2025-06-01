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
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/9-art')]"))
        )
        art_category.click()

        # Step 2: Wait for the category page to load
        content_wrapper = wait.until(EC.presence_of_element_located((By.ID, "content-wrapper")))
        if not content_wrapper:
            self.fail("Art category page did not load.")

        # Step 3: Locate the filter section for Composition and apply "Matt paper"
        try:
            filter_composition_matt_paper = wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//label[contains(., 'Matt paper')]/input")
                )
            )
            filter_composition_matt_paper.click()

            # Step 4: Wait for the filter to apply
            products_after_filter = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@id='js-product-list']//article")
                )
            )
            self.assertEqual(len(products_after_filter), 3, "Product count did not reduce to 3 after filter applied.")

            # Step 5: Locate and click the "Clear all" link
            wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='btn btn-secondary ok']")
                )
            ).click()

            # Step 6: Wait and assert that the number of products returns to the original count
            products_after_clear = wait.until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//div[@id='js-product-list']//article")
                )
            )
            self.assertEqual(len(products_after_clear), 7, "Product count did not return to 7 after clearing filters.")

        except Exception as e:
            self.fail(f"Failed during filter application process: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()