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
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.url)

        # 2. Click on the "Art" category in the top menu.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a"))
        )
        art_category_link.click()

        # 3. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category"))
        )

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section_xpath = "//section[@class='facet clearfix'][.//p[contains(text(), 'Composition')]]"
        filter_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, filter_section_xpath))
        )

        matt_paper_checkbox_xpath = filter_section_xpath + "//li//label[contains(., 'Matt paper')]//input[@type='checkbox']"
        matt_paper_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, matt_paper_checkbox_xpath))
        )
        matt_paper_checkbox.click()

        # 5. Wait for the filter to apply.
        WebDriverWait(driver, 20).until(
            lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div")) == 3
        )

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        product_count_after_filter = len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div"))
        self.assertEqual(product_count_after_filter, 3)

        # 7. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//div[@id='search_filters_wrapper']//a[contains(text(), 'Clear all')]"
        # Check if the clear all button exists before clicking
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//section[@id='js-active-search-filters']/ul/li/a[text()='Clear all']"))
            ).click()
        except:
            self.fail("Clear all button not found")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        WebDriverWait(driver, 20).until(
            lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div")) == 7
        )
        product_count_after_clear = len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='products row']/div"))
        self.assertEqual(product_count_after_clear, 7)

if __name__ == "__main__":
    unittest.main()