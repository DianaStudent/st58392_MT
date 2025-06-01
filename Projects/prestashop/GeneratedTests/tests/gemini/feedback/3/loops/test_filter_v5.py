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
        self.assertEqual(driver.current_url, self.url)

        # 2. Click on the "Art" category in the top menu.
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#category-9 > a.dropdown-item"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Art' category link: {e}")

        # 3. Wait for the category page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "category"))
            )
        except Exception as e:
            self.fail(f"Category page did not load correctly: {e}")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            matt_paper_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix'][.//p[text()='Composition']]//label[contains(., 'Matt paper')]/span/input"))
            )
            matt_paper_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Matt paper' checkbox: {e}")

        # 5. Wait for the filter to apply and assert that the number of product tiles is reduced from 7 to 3.
        try:
            WebDriverWait(driver, 20).until(lambda driver:
                len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")) == 3
            )
        except Exception as e:
            self.fail(f"Filter did not apply correctly: {e}")

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        product_tiles = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")
        self.assertEqual(len(product_tiles), 3)

        # 7. Locate and click the "Clear all" button to remove filters.
        try:
            # Find the "Clear all" link within the active search filters section
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#js-active-search-filters a"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Clear all' button: {e}")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        try:
            WebDriverWait(driver, 20).until(lambda driver:
                len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")) == 7
            )
        except Exception as e:
            self.fail(f"Clear all did not apply correctly: {e}")

        product_tiles_after_clear = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product col-xs-12 col-sm-6 col-xl-4']")
        self.assertEqual(len(product_tiles_after_clear), 7)

if __name__ == "__main__":
    unittest.main()