import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.url = "http://localhost:8080/en/"
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Click on the "Art" category in the top menu.
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Art' category link: {e}")

        # 2. Wait for the category page to load.
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list-header"))
            )
        except Exception as e:
            self.fail(f"Category page did not load correctly: {e}")

        # 3. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            matt_paper_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]//a[contains(text(), 'Matt paper')]/preceding-sibling::span/input"))
            )
            matt_paper_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Matt paper' checkbox: {e}")

        # 4. Wait for the filter to apply and assert that the number of product tiles is reduced from 7 to 3.
        try:
            WebDriverWait(driver, 20).until(lambda driver:
                len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[contains(@class, 'js-product product')]")) == 3
            )
            product_count_after_filter = len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[contains(@class, 'js-product product')]"))
            self.assertEqual(product_count_after_filter, 3, "Product count was not reduced to 3 after applying filter")
        except Exception as e:
            self.fail(f"Filter did not apply correctly or product count assertion failed: {e}")

        # 5. Locate and click the "Clear all" button to remove filters.
        try:
            clear_all_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Clear all' button: {e}")

        # 6. Wait and assert that the number of products returns to the original count - 7.
        try:
            WebDriverWait(driver, 20).until(lambda driver:
                len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[contains(@class, 'js-product product')]")) == 7
            )
            product_count_after_clear = len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div[contains(@class, 'js-product product')]"))
            self.assertEqual(product_count_after_clear, 7, "Product count did not return to 7 after clearing filters")
        except Exception as e:
            self.fail(f"Filters did not clear correctly or product count assertion failed: {e}")

if __name__ == "__main__":
    unittest.main()