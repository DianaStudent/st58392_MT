from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ProductFilterTestCase(unittest.TestCase):
    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the "Art" category in the top menu
        art_category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
        )
        art_category_link.click()

        # Step 3: Wait for the category page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "main#category"))
        )

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_section = wait.until(
            EC.presence_of_element_located((By.XPATH, "//section[.//p[text()='Composition']]"))
        )
        matt_paper_checkbox = composition_section.find_element(By.XPATH, ".//label[.//span[text()=' Matt paper ']]//input")
        driver.execute_script("arguments[0].click();", matt_paper_checkbox)

        # Step 6: Wait for the filter to apply
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products row']/div"))
        )

        # Step 7: Assert that the number of product tiles is reduced from 7 to 3
        filtered_products = driver.find_elements(By.XPATH, "//div[@class='products row']/div")
        if len(filtered_products) != 3:
            self.fail("Product count after applying the filter is not as expected.")

        # Step 8: Locate and click the "Clear all" button to remove filters
        clear_all_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-secondary ok']"))
        )
        driver.execute_script("arguments[0].click();", clear_all_button)

        # Step 9: Wait and assert that the number of products returns to the original count - 7
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='products row']/div"))
        )
        product_list_after_clearing = driver.find_elements(By.XPATH, "//div[@class='products row']/div")
        if len(product_list_after_clearing) != 7:
            self.fail("Product count after clearing the filter is not as expected.")
        
if __name__ == "__main__":
    unittest.main()