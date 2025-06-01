from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # 1. Open the home page - Done in setUp

        # 2. Click on the "Art" category in the top menu
        art_category_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]")))
        art_category_link.click()

        # 3. Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        filter_section = wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
        if not filter_section:
            self.fail("Filter section not found")

        matt_paper_checkbox_xpath = "//section[@class='facet clearfix']//p[text()='Composition']/following-sibling::ul//a[text()=' Matt paper ']/preceding-sibling::span/input[@type='checkbox']"
        matt_paper_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, matt_paper_checkbox_xpath)))
        matt_paper_checkbox.click()

        # 5. Wait for the filter to apply
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")) == 3)

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        product_tiles = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
        self.assertEqual(len(product_tiles), 3, "Number of product tiles is not 3 after applying filter")

        # 7. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[text()='Clear all']"
        clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_all_button_xpath)))
        clear_all_button.click()

        # 8. Wait and assert that the number of products returns to the original count - 7.
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")) == 7)

        product_tiles_after_clear = driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
        self.assertEqual(len(product_tiles_after_clear), 7, "Number of product tiles is not 7 after clearing filter")

if __name__ == "__main__":
    unittest.main()