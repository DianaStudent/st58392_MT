import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.url = "http://localhost:8080/en/"
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # Already done in setUp

        # 2. Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]")))
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

        matt_paper_checkbox_xpath = "//section[.//p[text()='Composition']]//label[.//text()[contains(., 'Matt paper')]]/span/input"
        matt_paper_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, matt_paper_checkbox_xpath)))
        if matt_paper_checkbox:
            matt_paper_checkbox.click()
        else:
            self.fail("Matt paper checkbox not found.")

        # 5. Wait for the filter to apply.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        product_count_element_xpath = "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"
        product_count_element = wait.until(EC.presence_of_element_located((By.XPATH, product_count_element_xpath)))
        if product_count_element:
            product_count_text = product_count_element.text
            self.assertEqual(product_count_text, "There are 3 products.")
        else:
            self.fail("Product count element not found.")

        # 7. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[text()='Clear all']"
        clear_all_button = wait.until(EC.presence_of_element_located((By.XPATH, clear_all_button_xpath)))

        if clear_all_button:
            clear_all_button.click()
        else:
            self.fail("Clear all button not found.")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        product_count_element = wait.until(EC.presence_of_element_located((By.XPATH, product_count_element_xpath)))
        if product_count_element:
            product_count_text = product_count_element.text
            self.assertEqual(product_count_text, "There are 7 products.")
        else:
            self.fail("Product count element not found after clearing filters.")

if __name__ == "__main__":
    unittest.main()