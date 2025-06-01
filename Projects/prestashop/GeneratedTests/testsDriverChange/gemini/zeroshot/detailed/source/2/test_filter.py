import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page (already done in setUp)

        # 2. Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a")))
        if art_category_link:
            art_category_link.click()
        else:
            self.fail("Art category link not found.")

        # 3. Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
        if not filter_section:
            self.fail("Filter section not found.")

        matt_paper_checkbox_xpath = "//section[@class='facet clearfix']/p[contains(text(), 'Composition')]/following-sibling::ul[@class='collapse']/li/label[contains(., 'Matt paper')]/span[@class='custom-checkbox']/input[@type='checkbox']"
        matt_paper_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, matt_paper_checkbox_xpath)))

        if matt_paper_checkbox:
            matt_paper_checkbox.click()
        else:
            self.fail("Matt paper checkbox not found or not clickable.")

        # 5. Wait for the filter to apply.
        product_count_locator = (By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p")
        wait.until(lambda driver: "3 products" in driver.find_element(*product_count_locator).text)

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        product_count_element = wait.until(EC.presence_of_element_located(product_count_locator))
        if product_count_element and product_count_element.text:
            self.assertEqual("There are 3 products.", product_count_element.text)
        else:
            self.fail("Product count element not found or empty.")

        # 7. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[contains(text(),'Clear all')]"
        clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_all_button_xpath)))

        if clear_all_button:
            clear_all_button.click()
        else:
            self.fail("Clear all button not found or not clickable.")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        wait.until(lambda driver: "7 products" in driver.find_element(*product_count_locator).text)
        product_count_element = wait.until(EC.presence_of_element_located(product_count_locator))
        if product_count_element and product_count_element.text:
            self.assertEqual("There are 7 products.", product_count_element.text)
        else:
            self.fail("Product count element not found or empty after clearing filters.")

if __name__ == "__main__":
    unittest.main()