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
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page - Done in setUp

        # 2. Click on the "Art" category in the top menu
        art_category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@id='category-9']/a[text()='Art']")))
        art_category_link.click()

        # 3. Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.ID, "category")))

        # 4. Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter_section = wait.until(EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix']/p[text()='Composition']")))
        if not composition_filter_section:
            self.fail("Filter section 'Composition' not found")

        matt_paper_checkbox_label = wait.until(EC.presence_of_element_located((By.XPATH, "//section[@class='facet clearfix']/ul[@id='facet_57074']//a[text()=' Matt paper ']/../span/input")))
        if not matt_paper_checkbox_label:
            self.fail("Matt paper checkbox not found")
        matt_paper_checkbox_label.click()

        # 5. Wait for the filter to apply and the product count to change
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()=' Matt paper ']")))

        # 6. Assert that the number of product tiles is reduced from 7 to 3
        product_count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")))
        if not product_count_element:
            self.fail("Product count element not found")

        product_count_text = product_count_element.text
        if not product_count_text:
            self.fail("Product count text is empty")

        expected_product_count_text = "There are 3 products."
        self.assertNotEqual(product_count_text, expected_product_count_text, f"Expected '{expected_product_count_text}', but got '{product_count_text}'")

        # 7. Locate and click the "Clear all" button to remove filters.
        clear_all_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Clear all")))
        if not clear_all_button:
            self.fail("Clear all button not found")
        clear_all_button.click()

        # 8. Wait and assert that the number of products returns to the original count - 7.
        wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()=' Matt paper ']")))

        product_count_element = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")))
        if not product_count_element:
            self.fail("Product count element not found")

        product_count_text = product_count_element.text
        if not product_count_text:
            self.fail("Product count text is empty")

        expected_product_count_text = "There are 7 products."
        self.assertEqual(product_count_text, expected_product_count_text, f"Expected '{expected_product_count_text}', but got '{product_count_text}'")

if __name__ == "__main__":
    unittest.main()