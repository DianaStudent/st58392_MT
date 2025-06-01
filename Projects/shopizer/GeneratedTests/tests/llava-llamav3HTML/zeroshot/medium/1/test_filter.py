import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.manager import ChromeDriverManager

class TestSeleniumFiltering(unittest.TestCase):
    def setUp(self):
        # Set up the WebDriver and navigate to the home page.
        driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver = driver
        self.driver.get('https://shopizer.com/')

    def tearDown(self):
        # Close the WebDriver after completing all tests.
        self.driver.quit()

    def test_filtering(self):
        # Click on the "Tables" tab to filter products.
        tables_tab = self.driver.find_element_by_css_selector('label[for="tab_tables"]')
        self.driver.execute_script(f'arguments[0].click();', tables_tab)

        # Verify that at least one product appears.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[contains("Adelect")]')))

        # Click on the "Chairs" tab to change the filter.
        chairs_tab = self.driver.find_element_by_css_selector('label[for="tab_chairs"]')
        self.driver.execute_script(f'arguments[0].click();', chairs_tab)

        # Verify that product list is updated.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[contains("Adelect")]')))

        # Click on the "All" tab to remove the filter.
        all_tab = self.driver.find_element_by_css_selector('label[for="tab_all"]')
        self.driver.execute_script(f'arguments[0].click();', all_tab)

        # Confirm that the full list of products is shown.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[contains("Adelect")]')))

    def test_filter_count(self):
        # Click on the "Tables" tab to filter products.
        tables_tab = self.driver.find_element_by_css_selector('label[for="tab_tables"]')
        self.driver.execute_script(f'arguments[0].click();', tables_tab)

        # Verify that at least one product appears.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[contains("Adelect")]')))

        # Get the initial count of products displayed.
        before_filter_count = self.driver.find_elements_by_css_selector('tr').count

        # Click on the "Chairs" tab to change the filter.
        chairs_tab = self.driver.find_element_by_css_selector('label[for="tab_chairs"]')
        self.driver.execute_script(f'arguments[0].click();', chairs_tab)

        # Verify that product list is updated and check that count changes.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[contains("Adelect")]')))

        # Get the count of products displayed after applying filters.
        after_filter_count = self.driver.find_elements_by_css_selector('tr').count

        # Confirm that the product count changes after applying and removing filters.
        self.assertTrue(before_filter_count != after_filter_count)

if __name__ == '__main__':
    unittest.main()