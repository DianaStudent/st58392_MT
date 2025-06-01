from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ArtCategoryFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_art_by_matt_paper(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the Home Page
        # Automatically done in setUp()
        
        # Step 2: Click on the "Art" category in the top menu
        art_category = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[@class='dropdown-item' and text()=' Art ']")))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h1[@class='h1' and text()='Art']")))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        filter_matt_paper = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(., ' Matt paper ')]//input[@type='checkbox']")))
        filter_matt_paper.click()

        # Step 5 & 6: Wait for the filter to apply
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature reviews-loaded']")) < 7)

        # Step 7: Assert that the number of product tiles is reduced from 7 to 3
        filtered_products = driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature reviews-loaded']")
        self.assertEqual(len(filtered_products), 3, "Product count after filter should be 3")

        # Step 8: Locate and click the "Clear all" button to remove filters
        clear_all_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(text(), ' Clear all ')]")))
        clear_all_button.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature reviews-loaded']")) == 7)
        all_products = driver.find_elements(By.XPATH, "//article[@class='product-miniature js-product-miniature reviews-loaded']")
        self.assertEqual(len(all_products), 7, "Product count after clearing filter should return to 7")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()