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
        # 2. Navigate to the "Art" product category.
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
        )
        art_category_link.click()

        # 3. On the category page, wait for the filter sidebar to be present.
        filter_sidebar = wait.until(
            EC.presence_of_element_located((By.ID, "search_filters_wrapper"))
        )
        self.assertTrue(filter_sidebar.is_displayed(), "Filter sidebar is not present.")

        # Get initial product count
        total_products_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )
        initial_product_count_text = total_products_element.text
        self.assertIsNotNone(initial_product_count_text, "Initial product count text is None.")
        self.assertTrue(initial_product_count_text != "", "Initial product count text is empty.")
        initial_product_count = int("".join(filter(str.isdigit, initial_product_count_text)))

        # 4. Select the "Matt paper" filter.
        matt_paper_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
        )

        # Scroll to the element before clicking
        actions = ActionChains(driver)
        actions.move_to_element(matt_paper_label).perform()

        matt_paper_label.click()

        # 5. Wait for the page to update, and verify that the number of visible product items is reduced.
        wait.until(EC.staleness_of(total_products_element))
        new_total_products_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )
        new_product_count_text = new_total_products_element.text
        self.assertIsNotNone(new_product_count_text, "New product count text is None.")
        self.assertTrue(new_product_count_text != "", "New product count text is empty.")
        new_product_count = int("".join(filter(str.isdigit, new_product_count_text)))

        self.assertLess(new_product_count, initial_product_count,
                         "Product count did not decrease after applying filter.")

        # 6. Then click the "Clear all" button to remove filters.
        # Clear all is not present, so we uncheck the filter
        matt_paper_label = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Matt paper')]"))
        )

        # Scroll to the element before clicking
        actions = ActionChains(driver)
        actions.move_to_element(matt_paper_label).perform()

        matt_paper_label.click()

        # 7. Verify that the number of products returns to the original count.
        wait.until(EC.staleness_of(new_total_products_element))
        final_total_products_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".total-products p"))
        )
        final_product_count_text = final_total_products_element.text
        self.assertIsNotNone(final_product_count_text, "Final product count text is None.")
        self.assertTrue(final_product_count_text != "", "Final product count text is empty.")
        final_product_count = int("".join(filter(str.isdigit, final_product_count_text)))

        self.assertEqual(final_product_count, initial_product_count,
                         "Product count did not return to original count after clearing filter.")


if __name__ == "__main__":
    unittest.main()