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

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        # 2. Click on the "Art" category in the top menu.
        try:
            art_category_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]")))
            art_category_link.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Art' category link: {e}")

        # 3. Wait for the category page to load.
        try:
            wait.until(EC.presence_of_element_located((By.ID, "js-product-list")))
        except Exception as e:
            self.fail(f"Category page did not load correctly: {e}")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            matt_paper_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//section[.//p[contains(text(), 'Composition')]]//label[.//text()[contains(., 'Matt paper')]]/span/input")))
            matt_paper_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Matt paper' checkbox: {e}")

        # 5. Wait for the filter to apply.
        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        try:
            wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 3)
            product_count = len(driver.find_elements(By.CLASS_NAME, "js-product"))
            self.assertEqual(product_count, 3, "Product count should be 3 after filter.")
        except Exception as e:
            self.fail(f"Filter did not apply correctly or product count is incorrect: {e}")

        # 7. Locate and click the "Clear all" button to remove filters.
        try:
            clear_all_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Clear all")))
            clear_all_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Clear all' button: {e}")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        try:
            wait.until(lambda driver: len(driver.find_elements(By.CLASS_NAME, "js-product")) == 7)
            product_count_after_clear = len(driver.find_elements(By.CLASS_NAME, "js-product"))
            self.assertEqual(product_count_after_clear, 7, "Product count should be 7 after clearing filters.")
        except Exception as e:
            self.fail(f"Filters did not clear correctly or product count is incorrect: {e}")

if __name__ == "__main__":
    unittest.main()