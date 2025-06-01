from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestSeleniumFilters(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_apply_and_clear_filters(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page.
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on the "Art" category in the top menu.
        art_category = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//li[@id='category-9']/a[contains(text(), 'Art')]")
        ))
        art_category.click()

        # Step 3: Wait for the category page to load.
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//header[@id='header']")  # Verifying header presence on the new page
        ))

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        composition_section = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//section[@id='search_filters']//section[contains(., 'Composition')]")
        ))
        matt_paper_checkbox = composition_section.find_element(By.XPATH, ".//label[contains(., 'Matt paper')]/span/input")
        if not matt_paper_checkbox:
            self.fail("Matt paper checkbox not found")
        
        # Click the checkbox to apply the filter
        matt_paper_checkbox.click()

        # Step 5: Wait for the filter to apply.
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='js-product-list']//div[contains(@class, 'products')]")
        ))

        # Step 6: Assert that the number of product tiles is reduced from 7 to 3.
        products = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@id='js-product-list']//div[contains(@class, 'product')]" )
        ))
        self.assertEqual(len(products), 3, "Product count after applying 'Matt paper' filter is not 3")

        # Step 7: Locate and click the "Clear all" button to remove filters.
        clear_all_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Clear all')]")
        if not clear_all_button:
            self.fail("Clear all button not found")
        clear_all_button.click()

        # Step 8: Wait and assert that the number of products returns to the original count - 7.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']")))
        products_after_clear = driver.find_elements(
            By.XPATH, "//div[@id='js-product-list']//div[contains(@class, 'product')]"
        )
        self.assertEqual(len(products_after_clear), 7, "Product count after clearing filters is not 7")

if __name__ == "__main__":
    unittest.main()