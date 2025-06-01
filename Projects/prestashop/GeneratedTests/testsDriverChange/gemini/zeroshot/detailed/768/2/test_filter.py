import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.url = "http://localhost:8080/en/"
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]")))
        art_category_link.click()

        # 3. Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
        if not filter_section:
            self.fail("Filter section not found")

        matt_paper_checkbox_xpath = "//section[.//p[text()='Composition']]//label[contains(., 'Matt paper')]/span/input"
        matt_paper_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, matt_paper_checkbox_xpath)))
        matt_paper_checkbox.click()

        # 6. Wait for the filter to apply.
        wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 3)

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        product_tiles = driver.find_elements(By.CLASS_NAME, "js-product")
        self.assertEqual(len(product_tiles), 3, "Product count after filter is not 3")

        # 8. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[text()='Clear all']"
        clear_all_button = wait.until(EC.presence_of_element_located((By.XPATH, clear_all_button_xpath)))
        driver.execute_script("arguments[0].click();", clear_all_button)

        # 9. Wait and assert that the number of products returns to the original count - 7.
        wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 7)
        product_tiles_after_clear = driver.find_elements(By.CLASS_NAME, "js-product")
        self.assertEqual(len(product_tiles_after_clear), 7, "Product count after clear all is not 7")

if __name__ == "__main__":
    unittest.main()