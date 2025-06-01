from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Art" category in the top menu.
        try:
            art_category_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Art' category link: {e}")

        # 3. Wait for the category page to load.
        try:
            wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list-header"))
            )
        except Exception as e:
            self.fail(f"Category page did not load correctly: {e}")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            filter_section = wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )

            matt_paper_checkbox = filter_section.find_element(
                By.XPATH, "//section[.//p[contains(text(), 'Composition')]]//label[contains(., 'Matt paper')]/span/input"
            )
            matt_paper_checkbox.click()

        except Exception as e:
            self.fail(f"Could not find or click 'Matt paper' checkbox: {e}")

        # 5. Wait for the filter to apply.
        try:
            wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
            )
        except Exception as e:
            self.fail(f"Filter 'Matt paper' did not apply correctly: {e}")

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        try:
            product_list = wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
            product_tiles = product_list.find_elements(By.CLASS_NAME, "js-product")
            self.assertEqual(len(product_tiles), 3, "Product count after filter is not 3")
        except Exception as e:
            self.fail(f"Could not verify product count after filter: {e}")

        # 7. Locate and click the "Clear all" button to remove filters.
        try:
            clear_all_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Clear all' button: {e}")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        try:
            wait.until(
                EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There are 7 products.')]"))
            )
            product_list = wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
            product_tiles = product_list.find_elements(By.CLASS_NAME, "js-product")
            self.assertEqual(len(product_tiles), 7, "Product count after clearing filter is not 7")
        except Exception as e:
            self.fail(f"Could not verify product count after clearing filter: {e}")

if __name__ == "__main__":
    unittest.main()