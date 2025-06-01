from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestProductFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def test_product_filters(self):
        driver = self.driver

        # Step 1: Open the home page.
        driver.get("http://localhost:8080/en/")

        # Verify that the home page is loaded by checking the presence of a known element
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "top-menu"))
            )
        except Exception as e:
            self.fail(f"Home page did not load properly: {str(e)}")

        # Step 2: Navigate to a product category (e.g., Art)
        category_link = driver.find_element(By.LINK_TEXT, "Art")
        category_link.click()

        # Verify navigation by checking the presence of a known element on the category page
        try:
            filter_sidebar = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_filters"))
            )
        except Exception as e:
            self.fail(f"Category page did not load properly: {str(e)}")

        # Step 3: Wait for the filter sidebar to be present
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar is not displayed")

        # Step 4: Select a filter using label-based selection (e.g., Composition - Matt paper)
        composition_filter_label = driver.find_element(By.XPATH, "//label[contains(., 'Matt paper')]")
        if not composition_filter_label:
            self.fail("Matt paper filter label is missing")

        composition_checkbox = composition_filter_label.find_element(By.TAG_NAME, "input")
        composition_checkbox.click()

        # Step 5: Wait for the page to update and verify that the number of visible product items is reduced
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product"))
            )
            products_after_filter = driver.find_elements(By.CSS_SELECTOR, ".js-product")
            self.assertLess(len(products_after_filter), 7, "Filter did not reduce the number of products")
        except Exception as e:
            self.fail(f"Error verifying filtered product count: {str(e)}")

        # Step 6: Clear filters
        try:
            clear_filter_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Clear all')]")
            clear_filter_button.click()
        except Exception as e:
            self.fail(f"Clear all button is not found: {str(e)}")

        # Step 7: Verify number of products return to original count
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".js-product"))
            )
            products_after_clear = driver.find_elements(By.CSS_SELECTOR, ".js-product")
            self.assertEqual(len(products_after_clear), 7, "Product count did not return to original after clearing filters")
        except Exception as e:
            self.fail(f"Error verifying unfiltered product count: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()