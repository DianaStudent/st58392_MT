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

        # Navigate to the "Art" category page
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to Art category: {e}")

        # Wait for the filter sidebar to load
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
            )
        except Exception as e:
            self.fail(f"Filter sidebar did not load: {e}")

        # Get the initial product count
        try:
            initial_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            initial_product_count_text = initial_product_count_element.text
            initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))
        except Exception as e:
            self.fail(f"Could not get initial product count: {e}")

        # Select the "Matt paper" filter
        try:
            matt_paper_label = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
            )
            matt_paper_label.click()
        except Exception as e:
            self.fail(f"Could not select 'Matt paper' filter: {e}")

        # Wait for the filter to apply and the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after applying filter: {e}")

        # Get the updated product count
        try:
            updated_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            updated_product_count_text = updated_product_count_element.text
            updated_product_count = int("".join(filter(str.isdigit, updated_product_count_text)))
        except Exception as e:
            self.fail(f"Could not get updated product count: {e}")

        # Verify that the product count has changed
        self.assertNotEqual(initial_product_count, updated_product_count,
                             "Product count did not change after applying filter")

        # Clear the filter (navigate back to the Art category)
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not navigate back to Art category: {e}")

        # Wait for the filter to clear and the product list to update
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
        except Exception as e:
            self.fail(f"Product list did not update after clearing filter: {e}")

        # Get the final product count
        try:
            final_product_count_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
            )
            final_product_count_text = final_product_count_element.text
            final_product_count = int("".join(filter(str.isdigit, final_product_count_text)))
        except Exception as e:
            self.fail(f"Could not get final product count: {e}")

        # Verify that the product count has returned to the initial count
        self.assertEqual(initial_product_count, final_product_count,
                         "Product count did not return to initial count after clearing filter")


if __name__ == "__main__":
    unittest.main()