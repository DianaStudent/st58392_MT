import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://localhost:8080/en/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Click on the "Art" category in the top menu.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']/li/a[text()='Art']"))
        )
        art_category_link.click()

        # 2. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category"))
        )

        # 3. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        matt_paper_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'facet') and .//p[text()='Composition']]//a[text()=' Matt paper ']/../span/input"))
        )
        matt_paper_checkbox.click()

        # 4. Wait for the filter to apply.
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(By.XPATH, "//section[contains(@class, 'facet') and .//p[text()='Composition']]//a[text()=' Matt paper ']/span[contains(@class, 'magnitude')]")
        )

        # 5. Assert that the number of product tiles is reduced to 3.
        product_count_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"))
        )
        if product_count_element:
            product_count_text = product_count_element.text
            if product_count_text:
                self.assertEqual("There are 3 products.", product_count_text)
            else:
                self.fail("Product count text is empty.")
        else:
            self.fail("Product count element not found.")

        # 6. Locate and click the "Clear all" button to remove filters.
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 7. Wait and assert that the number of products returns to the original count - 7.
        WebDriverWait(driver, 20).until(
            lambda driver: driver.find_element(By.XPATH, "//section[contains(@class, 'facet') and .//p[text()='Composition']]//a[text()=' Matt paper ']/span[contains(@class, 'magnitude')]")
        )
        product_count_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='js-product-list-top']/div[@class='col-lg-5 hidden-sm-down total-products']/p"))
        )
        if product_count_element:
            product_count_text = product_count_element.text
            if product_count_text:
                self.assertEqual("There are 7 products.", product_count_text)
            else:
                self.fail("Product count text is empty.")
        else:
            self.fail("Product count element not found.")


if __name__ == "__main__":
    unittest.main()