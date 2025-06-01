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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Art" category in the top menu.
        try:
            art_category_link = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'Art' category link: {e}")

        # 3. Wait for the category page to load.
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list-header"))
            )
        except Exception as e:
            self.fail(f"Failed to load Art category page: {e}")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            filter_section = self.wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Failed to locate filter section: {e}")

        try:
            matt_paper_checkbox_label = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//section[.//p[text()='Composition']]//label[contains(., 'Matt paper')]//input[@type='checkbox']"))
            )
            matt_paper_checkbox_label.click()
        except Exception as e:
            self.fail(f"Failed to click 'Matt paper' checkbox: {e}")

        # 5. Do not use dynamic IDs. Use XPath or CSS selectors based on `data-name` and label text. (Done above)

        # 6. Wait for the filter to apply.
        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        try:
            products = self.wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product.product"))
            )
            self.assertEqual(len(products), 7, "Product count was not 7 initially")
        except Exception as e:
            self.fail(f"Failed to assert initial product count: {e}")

        try:
            self.wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".js-product.product")) == 3)
            products = self.driver.find_elements(By.CSS_SELECTOR, ".js-product.product")
            self.assertEqual(len(products), 3, "Product count was not reduced to 3 after applying filter")
        except Exception as e:
            self.fail(f"Failed to assert product count after filter application: {e}")

        # 8. Locate and click the "Clear all" button to remove filters.
        # Locate the "Clear all" link
        try:
            clear_all_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'Clear all' button: {e}")

        # 9. Wait and assert that the number of products returns to the original count - 7.
        try:
            self.wait.until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, ".js-product.product")) == 7)
            products = self.driver.find_elements(By.CSS_SELECTOR, ".js-product.product")
            self.assertEqual(len(products), 7, "Product count did not return to 7 after clearing filters")
        except Exception as e:
            self.fail(f"Failed to assert product count after clearing filters: {e}")


if __name__ == "__main__":
    unittest.main()