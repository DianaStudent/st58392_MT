import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_product_filter(self):
        # Step 1: Open the home page
        self.driver.get('http://localhost/')

        # Step 2: Click on the "Tables" tab to filter products
        tables_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='tables']"))
        )
        tables_tab.click()

        # Step 3: Verify that at least one product appears
        tables_tab_content = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='tabpanel' and @aria-hidden='false']"))
        )
        products = tables_tab_content.find_elements(By.CLASS_NAME, 'product-wrap-2')
        if len(products) == 0:
            self.fail('No product displayed after clicking on "Tables"')

        # Step 4: Click on the "Chairs" tab to change the filter
        chairs_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='chairs']"))
        )
        chairs_tab.click()

        # Step 5: Verify that product list is updated
        chairs_tab_content = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='tabpanel' and @aria-hidden='false']"))
        )
        products = chairs_tab_content.find_elements(By.CLASS_NAME, 'product-wrap-2')
        if len(products) == 0:
            self.fail('No product displayed after clicking on "Chairs"')

        # Step 6: Click "All" to remove the filter
        all_tab = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-rb-event-key='all']"))
        )
        all_tab.click()

        # Step 7: Confirm that the full list of products is shown
        all_tab_content = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='tabpanel' and @aria-hidden='false']"))
        )
        products = all_tab_content.find_elements(By.CLASS_NAME, 'product-wrap-2')
        if len(products) == 0:
            self.fail('No product displayed after clicking on "All"')
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()