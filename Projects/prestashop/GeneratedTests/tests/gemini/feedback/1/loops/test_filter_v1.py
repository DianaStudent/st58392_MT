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
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_product_filter(self):
        driver = self.driver
        driver.get(self.url)

        # 1. Click on the "Art" category in the top menu.
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Art' and @class='dropdown-item']"))
        )
        art_category_link.click()

        # 2. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category"))
        )

        # 3. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='search_filters_wrapper']"))
        )

        if not filter_section:
            self.fail("Filter section not found.")

        matt_paper_checkbox_xpath = "//section[@class='facet clearfix']/p[text()='Composition']/following-sibling::div//a[text()=' Matt paper ']/preceding-sibling::span/input[@type='checkbox']"

        matt_paper_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, matt_paper_checkbox_xpath))
        )

        if not matt_paper_checkbox:
            self.fail("Matt paper checkbox not found.")

        matt_paper_checkbox.click()

        # 4. Wait for the filter to apply and Assert that the number of product tiles is reduced from 7 to 3.
        WebDriverWait(driver, 20).until(
            lambda driver: EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p"),
                "There are 3 products."
            )(driver)
        )

        product_count_element = driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")
        product_count_text = product_count_element.text
        if not product_count_text:
            self.fail("Product count text is empty.")
        self.assertEqual(product_count_text, "There are 3 products.")

        # 5. Locate and click the "Clear all" button to remove filters.
        clear_all_button_xpath = "//a[text()='Clear all']"
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, clear_all_button_xpath))
        )
        if not clear_all_button:
            self.fail("Clear all button not found.")
        clear_all_button.click()

        # 6. Wait and assert that the number of products returns to the original count - 7.
        WebDriverWait(driver, 20).until(
            lambda driver: EC.text_to_be_present_in_element(
                (By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p"),
                "There are 7 products."
            )(driver)
        )

        product_count_element = driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")
        product_count_text = product_count_element.text
        if not product_count_text:
            self.fail("Product count text is empty.")
        self.assertEqual(product_count_text, "There are 7 products.")

if __name__ == "__main__":
    unittest.main()