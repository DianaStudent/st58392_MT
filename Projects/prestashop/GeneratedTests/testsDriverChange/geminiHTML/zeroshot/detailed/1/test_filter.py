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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Art" category in the top menu.
        try:
            art_category_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Failed to click 'Art' category link: {e}")

        # 3. Wait for the category page to load.
        try:
            self.wait.until(
                EC.presence_of_element_located((By.ID, "js-product-list"))
            )
        except Exception as e:
            self.fail(f"Failed to load product list on category page: {e}")

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        try:
            matt_paper_checkbox_xpath = "//section[.//p[contains(text(), 'Composition')]]//label[contains(., 'Matt paper')]/span/input"
            matt_paper_checkbox = self.wait.until(
                EC.presence_of_element_located((By.XPATH, matt_paper_checkbox_xpath))
            )
            matt_paper_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to click 'Matt paper' checkbox: {e}")

        # 5. Wait for the filter to apply.
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div"))
            )
        except Exception as e:
            self.fail(f"Failed to wait for the filter to apply: {e}")

        # 6. Assert that the number of product tiles is reduced from 7 to 3.
        try:
            product_tiles = self.driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
            self.assertEqual(len(product_tiles), 3, "Product count after filtering is not 3")
        except Exception as e:
            self.fail(f"Failed to assert product count after filtering: {e}")

        # 7. Locate and click the "Clear all" button to remove filters.
        try:
            clear_all_button_xpath = "//a[contains(text(), 'Clear all')]"
            clear_all_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, clear_all_button_xpath))
            )
            clear_all_button.click()
        except:
            print("Clear all button not found. Trying to proceed without clearing filters.")

        # 8. Wait and assert that the number of products returns to the original count - 7.
        try:
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div"))
            )
            product_tiles_after_clear = self.driver.find_elements(By.XPATH, "//div[@id='js-product-list']/div[@class='products row']/div")
            self.assertEqual(len(product_tiles_after_clear), 7, "Product count after clearing filters is not 7")
        except Exception as e:
            self.fail(f"Failed to assert product count after clearing filters: {e}")


if __name__ == "__main__":
    unittest.main()