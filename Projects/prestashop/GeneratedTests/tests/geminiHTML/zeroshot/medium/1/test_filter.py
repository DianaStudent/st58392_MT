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

        # 1. Open the home page. (Done in setUp)

        # 2. Navigate to the 'Art' product category.
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Art']"))
        )
        art_category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar not present")

        # Get the initial product count
        total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        self.assertIsNotNone(total_products_element, "Total products element not found")
        self.assertNotEqual(total_products_element.text, "", "Total products element is empty")

        initial_product_count_text = total_products_element.text
        print(f"Initial product count: {initial_product_count_text}")

        # 4. Select the 'Matt paper' filter under 'Composition' using label-based selection.
        composition_section = wait.until(
            EC.presence_of_element_located((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]"))
        )

        self.assertIsNotNone(composition_section, "Composition section not found")

        matt_paper_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]//a[contains(text(), 'Matt paper')]"))
        )

        self.assertIsNotNone(matt_paper_label, "Matt paper label not found")

        matt_paper_checkbox = wait.until(
            EC.presence_of_element_located((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]//a[contains(text(), 'Matt paper')]/ancestor::label//input[@type='checkbox']"))
        )

        self.assertIsNotNone(matt_paper_checkbox, "Matt paper checkbox not found")

        driver.execute_script("arguments[0].click();", matt_paper_checkbox)

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        wait.until(EC.staleness_of(total_products_element))

        new_total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        self.assertIsNotNone(new_total_products_element, "New total products element not found")
        self.assertNotEqual(new_total_products_element.text, "", "New total products element is empty")

        new_product_count_text = new_total_products_element.text
        print(f"New product count: {new_product_count_text}")

        self.assertNotEqual(initial_product_count_text, new_product_count_text, "Product count did not change after filtering")

        # 6. Then click the "Clear all" button to remove filters.
        # Locate the "Clear all" link and click it
        try:
            clear_all_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Clear all"))
            )
            clear_all_link.click()
        except:
            self.fail("Clear all link not found or not clickable")

        # 7. Verify that the number of products returns to the original count.
        wait.until(EC.staleness_of(new_total_products_element))

        final_total_products_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "total-products"))
        )

        self.assertIsNotNone(final_total_products_element, "Final total products element not found")
        self.assertNotEqual(final_total_products_element.text, "", "Final total products element is empty")

        final_product_count_text = final_total_products_element.text
        print(f"Final product count: {final_product_count_text}")

        self.assertEqual(initial_product_count_text, final_product_count_text, "Product count did not return to original after clearing filters")


if __name__ == "__main__":
    unittest.main()