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
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a[text()='Art']"))
        )
        art_category_link.click()

        # 2. Wait for the category page to load.
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "category"))
        )

        # 3. Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        filter_section = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//section[.//p[text()='Composition']]"))
        )

        matt_paper_checkbox_label = WebDriverWait(filter_section, 20).until(
            EC.presence_of_element_located((By.XPATH, ".//label[.//a[text()=' Matt paper ']]/span[@class='custom-checkbox']/input"))
        )
        matt_paper_checkbox_label.click()

        # 4. Wait for the filter to apply and assert that the number of product tiles is reduced from 7 to 3.
        WebDriverWait(driver, 20).until(lambda driver:
            "There are 3 products." in driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p").text
        )
        product_count_element = driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")
        if product_count_element and product_count_element.text:
            self.assertEqual("There are 3 products.", product_count_element.text)
        else:
            self.fail("Product count element not found or empty.")

        # 5. Locate and click the "Clear all" button to remove filters.
        # Use a more robust selector for "Clear all"
        clear_all_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Clear all"))
        )
        clear_all_button.click()

        # 6. Wait and assert that the number of products returns to the original count - 7.
        WebDriverWait(driver, 20).until(lambda driver:
            "There are 7 products." in driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p").text
        )
        product_count_element = driver.find_element(By.XPATH, "//div[@class='col-lg-5 hidden-sm-down total-products']/p")
        if product_count_element and product_count_element.text:
            self.assertEqual("There are 7 products.", product_count_element.text)
        else:
            self.fail("Product count element not found or empty after filter removal.")

if __name__ == "__main__":
    unittest.main()