import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class FilterTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_filter_by_composition(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page.
        driver.get("http://localhost:8080/en/")

        # Step 2: Click on the "Art" category in the top menu.
        art_category = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        art_category.click()

        # Step 3: Wait for the category page to load by checking for the filter section.
        wait.until(EC.presence_of_element_located((By.ID, "search_filters")))

        # Step 4: Apply the checkbox "Matt paper" under "Composition".
        matt_paper_checkbox = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[contains(., 'Matt paper')]//input[@type='checkbox']")))
        matt_paper_checkbox.click()

        # Step 5: Wait for the filter to apply and assert that the number of product tiles is reduced.
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'js-product')]")) == 3)

        # Verify the number of products is 3
        product_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'js-product')]")
        if not product_elements:
            self.fail("Product elements not found after applying filter.")
        self.assertEqual(len(product_elements), 3, "Product count did not reduce to 3 after filtering.")

        # Step 6: Click the "Clear all" button to remove filters.
        clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Clear all')]")))
        clear_all_button.click()

        # Step 7: Wait and assert that the number of products returns to the original count.
        wait.until(lambda driver: len(driver.find_elements(By.XPATH, "//div[contains(@class, 'js-product')]")) == 7)

        product_elements_after_clear = driver.find_elements(By.XPATH, "//div[contains(@class, 'js-product')]")
        if not product_elements_after_clear:
            self.fail("Product elements not found after clearing filters.")
        self.assertEqual(len(product_elements_after_clear), 7, "Product count did not return to 7 after clearing filters.")


if __name__ == "__main__":
    unittest.main()