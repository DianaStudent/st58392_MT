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
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver

        # Navigate to the 'Art' category page
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Get initial product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = total_products_element.text
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))

        except Exception as e:
            self.fail(f"Failed to get initial product count: {e}")

        # Apply the 'Matt paper' filter
        try:
            composition_section = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]"))
            )
            matt_paper_label = composition_section.find_element(By.XPATH, ".//a[contains(text(), 'Matt paper')]")

            # Find the input element associated with the label
            input_id = matt_paper_label.get_attribute("href").split("q=Composition-Matt+paper")[0].split("/")[-1]
            input_element = composition_section.find_element(By.ID, "facet_input_57074_0")
            driver.execute_script("arguments[0].click();", input_element)

        except Exception as e:
            self.fail(f"Failed to apply 'Matt paper' filter: {e}")

        # Wait for the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.staleness_of(total_products_element)
            )
        except Exception as e:
            self.fail(f"Product list did not update after applying filter: {e}")

        # Get the updated product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            updated_product_count_text = total_products_element.text
            updated_product_count = int("".join(filter(str.isdigit, updated_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get updated product count: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, updated_product_count, "Product count did not change after applying filter")

        #Clear Filter
        try:
            driver.get("http://localhost:8080/en/9-art")
        except Exception as e:
            self.fail(f"Failed to navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Wait for the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.staleness_of(total_products_element)
            )
        except Exception as e:
            self.fail(f"Product list did not update after applying filter: {e}")

        # Get the updated product count
        try:
            total_products_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            after_clear_product_count_text = total_products_element.text
            after_clear_product_count = int("".join(filter(str.isdigit, after_clear_product_count_text)))
        except Exception as e:
            self.fail(f"Failed to get updated product count: {e}")

        # Verify that the product count has changed
        self.assertEqual(initial_product_count, after_clear_product_count, "Product count did not change after clear filter")


if __name__ == "__main__":
    unittest.main()