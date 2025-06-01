import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page - Done in setUp

        # 2. Click on the "Art" category in the top menu.
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Art']")))
        if art_category_link:
            art_category_link.click()
        else:
            self.fail("Art category link not found.")

        # 3. Wait for the category page to load.
        wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = wait.until(EC.presence_of_element_located((By.ID, "search_filters_wrapper")))
        if not filter_section:
            self.fail("Filter section not found.")

        matt_paper_checkbox_xpath = "//p[text()='Composition']/following-sibling::ul//a[text()=' Matt paper ']/preceding-sibling::span/input[@type='checkbox']"
        matt_paper_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, matt_paper_checkbox_xpath)))

        if matt_paper_checkbox:
            matt_paper_checkbox.click()
        else:
            self.fail("Matt paper checkbox not found or not clickable.")

        # 5. Do not use dynamic IDs. Use XPath or CSS selectors based on data-name and label text. - Done

        # 6. Wait for the filter to apply.
        initial_product_count = 7
        wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) < initial_product_count)

        # 7. Assert that the number of product tiles is reduced from 7 to 3.
        filtered_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        self.assertEqual(filtered_product_count, 3, f"Expected 3 products, but got {filtered_product_count}")

        # 8. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[text()='Clear all']"
        clear_all_button = wait.until(EC.element_to_be_clickable((By.XPATH, clear_all_button_xpath)))

        if clear_all_button:
            clear_all_button.click()
        else:
            self.fail("Clear all button not found or not clickable.")

        # 9. Wait and assert that the number of products returns to the original count - 7.
        wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) > filtered_product_count)
        final_product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
        self.assertEqual(final_product_count, initial_product_count, f"Expected {initial_product_count} products, but got {final_product_count}")

if __name__ == "__main__":
    unittest.main()