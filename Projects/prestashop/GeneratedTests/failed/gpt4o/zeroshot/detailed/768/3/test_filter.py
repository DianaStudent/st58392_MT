from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1 and 2: Click on "Art" category from top menu
        art_category = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Art']")))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Art']")))

        # Step 4: Locate and apply the "Matt paper" filter under "Composition"
        filter_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[@data-name='Composition']")))
        matt_paper_checkbox = filter_section.find_element(By.XPATH, ".//label[contains(., 'Matt paper')]/input")
        matt_paper_checkbox.click()

        # Step 5: Wait for the filter to apply
        wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) == 3)

        # Step 6 and 7: Assert the number of products is 3
        product_tiles = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(product_tiles), 3, "Product tiles count after applying filter is not 3.")

        # Step 8: Locate and click the "Clear all" button
        clear_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Clear all')]")))
        clear_button.click()

        # Step 9: Wait and assert the number of products returns to 7
        wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".product-miniature")) == 7)
        product_tiles_after_clear = driver.find_elements(By.CSS_SELECTOR, ".product-miniature")
        self.assertEqual(len(product_tiles_after_clear), 7, "Product tiles count after clearing filter is not 7.")

if __name__ == "__main__":
    unittest.main()