from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"

    def test_filter_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the home page.
        driver.get(self.base_url)

        # Step 2: Click on the "Art" category in the top menu.
        art_category = wait.until(
            EC.presence_of_element_located((By.XPATH, "//ul[@id='top-menu']//a[contains(text(),'Art')]"))
        )
        art_category.click()

        # Step 3: Wait for the category page to load.
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Art')]"))
        )

        # Step 4 and 5: Locate the filter section and apply the checkbox "Matt paper" under "Composition".
        matt_paper_filter = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[@data-name='Composition']//label[contains(text(),'Matt paper')]//input"))
        )
        matt_paper_filter.click()

        # Step 6 and 7: Wait for the filter to apply.
        wait.until(
            lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")) == 3
        )
        products_after_filter = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")
        self.assertEqual(len(products_after_filter), 3, "Product count after filter should be 3.")

        # Step 8: Locate and click the "Clear all" button to remove filters.
        clear_all_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='btn btn-secondary' and contains(text(), 'Clear')]"))
        )
        clear_all_button.click()

        # Step 9: Wait and assert that the number of products returns to the original count - 7.
        wait.until(
            lambda driver: len(driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")) == 7
        )
        products_after_clear = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//article")
        self.assertEqual(len(products_after_clear), 7, "Product count after clearing filter should return to 7.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()