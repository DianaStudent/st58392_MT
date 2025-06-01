from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        
        # Open the home page and click on the "Art" category
        art_category_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Art']"))
        )
        art_category_link.click()

        # Wait for the category page to load
        self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.category-art"))
        )

        # Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_matt_paper = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//label[contains(., 'Composition')]/following-sibling::ul//label[contains(text(), 'Matt paper')]//input")
            )
        )
        
        self.wait.until(EC.element_to_be_clickable(composition_matt_paper)).click()

        # Wait for the filter to apply - assert the number of product tiles is reduced from 7 to 3
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@id,'js-product-list')]//article[3]")
            )
        )
        products_filtered = driver.find_elements(By.XPATH, "//*[contains(@id,'js-product-list')]//article")
        self.assertEqual(len(products_filtered), 3, "Product count after filtering should be 3.")

        # Clear filter and assert product count returns to 7
        clear_all_button = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//section[@id='js-active-search-filters']//button[contains(@class,'close')]")
            )
        )
        self.wait.until(EC.element_to_be_clickable(clear_all_button)).click()

        # Wait and assert that the number of products returns to the original count - 7
        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[contains(@id,'js-product-list')]//article[7]")
            )
        )
        products_back = driver.find_elements(By.XPATH, "//*[contains(@id,'js-product-list')]//article")
        self.assertEqual(len(products_back), 7, "Product count after clearing filters should return to 7.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()