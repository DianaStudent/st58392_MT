import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # 2. Navigate to a product category.
        try:
            category_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to the Art category: {e}")

        # 3. On the category page, wait for the filter sidebar to be present.
        try:
            filter_sidebar = wait.until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar not found: {e}")

        # 4. Select the filter using label-based selection.
        try:
            composition_filter_section = wait.until(
                EC.presence_of_element_located((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]"))
            )
            composition_filter_label = composition_filter_section.find_element(By.XPATH, ".//a[contains(text(), 'Matt paper')]")
            
            # Find the input element associated with the label and click it
            input_id = composition_filter_label.get_attribute("href").split('q=Composition-')[-1].replace('+',' ')
            input_element = driver.find_element(By.XPATH, f"//a[contains(text(), '{input_id}')]/ancestor::li//input[@type='checkbox']")
            driver.execute_script("arguments[0].click();", input_element)
            
        except Exception as e:
            self.fail(f"Could not select the 'Matt paper' filter: {e}")

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        try:
            initial_product_count_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = initial_product_count_element.text
            if not initial_product_count_text:
                self.fail("Initial product count text is empty.")
            
            initial_product_count = int(initial_product_count_text.split(' ')[2])

            wait.until(
                EC.staleness_of(initial_product_count_element)
            )

            updated_product_count_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            updated_product_count_text = updated_product_count_element.text
            if not updated_product_count_text:
                self.fail("Updated product count text is empty.")
            updated_product_count = int(updated_product_count_text.split(' ')[2])

            self.assertLess(updated_product_count, initial_product_count,
                            "Product count did not decrease after applying the filter.")

        except Exception as e:
            self.fail(f"Could not verify product count after filtering: {e}")

        # 6. Then click the "Clear all" button to remove filters.
        try:
            # Find the filter section containing the 'Matt paper' filter
            filter_section = wait.until(
                EC.presence_of_element_located((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]"))
            )
            
            # Find the input element associated with the label and click it
            input_id = composition_filter_label.get_attribute("href").split('q=Composition-')[-1].replace('+',' ')
            input_element = driver.find_element(By.XPATH, f"//a[contains(text(), '{input_id}')]/ancestor::li//input[@type='checkbox']")
            driver.execute_script("arguments[0].click();", input_element)
            
        except Exception as e:
            self.fail(f"Could not clear the filters: {e}")

        # 7. Verify that the number of products returns to the original count.
        try:
            wait.until(
                EC.staleness_of(updated_product_count_element)
            )

            final_product_count_element = wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            final_product_count_text = final_product_count_element.text
            if not final_product_count_text:
                self.fail("Final product count text is empty.")
            final_product_count = int(final_product_count_text.split(' ')[2])

            self.assertEqual(final_product_count, initial_product_count,
                             "Product count did not return to the original count after clearing filters.")

        except Exception as e:
            self.fail(f"Could not verify product count after clearing filters: {e}")


if __name__ == "__main__":
    unittest.main()