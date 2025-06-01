import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_product_filter(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        home_page_title = driver.title
        if not home_page_title:
            self.fail("Home page failed to load.")

        # Step 2: Click on the "Art" category in the top menu.
        art_category_link = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Art')]"))
        )
        art_category_link.click()

        # Step 3: Wait for the category page to load
        category_title = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Art')]"))
        )
        if not category_title:
            self.fail("Category page failed to load.")

        # Step 4: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        matt_paper_checkbox = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//a[contains(@href, 'Composition-Matt+paper')]/preceding-sibling::input")
            )
        )
        matt_paper_checkbox.click()

        # Step 6: Wait for the filter to apply
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']")))

        # Step 7: Assert that the number of product tiles is reduced from 7 to 3.
        products = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.js-product"))
        )
        if not products or len(products) != 3:
            self.fail("Expected 3 products after filter, found: {}".format(len(products)))

        # Step 8: Locate and click the "Clear all" button to remove filters.
        clear_all_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        )
        clear_all_button.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7.
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list']")))
        final_products = driver.find_elements(By.CSS_SELECTOR, "div.js-product")
        if not final_products or len(final_products) != 7:
            self.fail("Expected 7 products after clearing filters, found: {}".format(len(final_products)))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()