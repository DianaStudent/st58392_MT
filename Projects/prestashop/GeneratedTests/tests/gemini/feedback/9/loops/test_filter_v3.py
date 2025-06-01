import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # 2. Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art') and contains(@class, 'dropdown-item')]")))
        art_category_link.click()

        # 3. Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "category")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_sidebar = wait.until(EC.presence_of_element_located((By.ID, "left-column")))
        self.assertIsNotNone(filter_sidebar, "Filter sidebar not found.")

        # Select "Matt paper" checkbox
        matt_paper_checkbox_xpath = "//section[@class='facet clearfix']//p[contains(text(), 'Composition')]/following-sibling::ul//a[contains(text(), 'Matt paper')]/../span[@class='custom-checkbox']/input[@type='checkbox']"
        matt_paper_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, matt_paper_checkbox_xpath)))
        matt_paper_checkbox.click()

        # 5. Do not use dynamic IDs. Use XPath or CSS selectors based on data-name and label text.
        # 6. Wait for the filter to apply.
        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        product_count_locator = (By.XPATH, "//div[@id='js-product-list-top']//p[contains(text(), 'product')]")
        wait.until(lambda driver: "3 products" in driver.find_element(*product_count_locator).text)
        product_count_element = driver.find_element(*product_count_locator)
        self.assertIn("3 products", product_count_element.text, "Product count is not 3 after applying filter.")

        # 8. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//ul[@class='active-facets']/li[@class='filter-block']/a[contains(text(),'Clear all')]"
        try:
            clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_all_button_xpath)))
            clear_all_button.click()
        except:
            self.fail("Clear all button not found or not clickable")

        # 9. Wait and assert that the number of products returns to the original count - 7.
        wait.until(lambda driver: "7 products" in driver.find_element(*product_count_locator).text)
        product_count_element = driver.find_element(*product_count_locator)
        self.assertIn("7 products", product_count_element.text, "Product count is not 7 after clearing filters.")

if __name__ == "__main__":
    unittest.main()