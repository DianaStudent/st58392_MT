import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:8080/en/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.url, "Failed to open the home page.")

        # 2. Click on the "Art" category in the top menu.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category_link.click()

        # 3. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category"))
        )
        self.assertEqual(driver.current_url, "http://localhost:8080/en/9-art", "Failed to open the Art category page.")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        if not filter_section:
            self.fail("Filter section not found.")

        # Find the "Matt paper" checkbox within the "Composition" filter section and click it
        matt_paper_checkbox_label = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix']/p[text()='Composition']/following-sibling::ul[@class='collapse']/li/label/a[text()=' Matt paper ']"))
        )

        if not matt_paper_checkbox_label:
            self.fail("Matt paper checkbox label not found.")

        matt_paper_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix']/p[text()='Composition']/following-sibling::ul[@class='collapse']/li/label/span[@class='custom-checkbox']/input"))
        )

        matt_paper_checkbox.click()

        # 6. Wait for the filter to apply.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']"))
        )

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        product_tiles = driver.find_elements(By.XPATH, "//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")
        self.assertEqual(len(product_tiles), 3, "Product count is not 3 after applying filter.")

        # 8. Locate and click the "Clear all" button to remove filters.
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[@id='js-active-search-filters']/ul[@class='active-filters']/li/a"))
        )
        if not clear_all_button:
            self.fail("Clear all button not found.")
        clear_all_button.click()

        # 9. Wait and assert that the number of products returns to the original count - 7.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']"))
        )

        product_tiles_after_clear = driver.find_elements(By.XPATH, "//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")
        self.assertEqual(len(product_tiles_after_clear), 7, "Product count is not 7 after clearing filters.")

if __name__ == "__main__":
    unittest.main()