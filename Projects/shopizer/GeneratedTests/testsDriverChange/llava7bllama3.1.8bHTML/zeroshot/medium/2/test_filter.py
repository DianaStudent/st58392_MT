from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopizer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # Assuming the shop is hosted locally
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "nav-tabs")))

    def tearDown(self):
        self.driver.quit()

    def test_shopizer_filtering(self):

        # Click on "Tables" tab to filter products
        table_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@data-name='tables']")))
        table_tab.click()

        # Verify that at least one product appears after applying the filter
        products_after_filtering = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='col-sm-4 col-xs-6']/div[1]")))
        self.assertGreater(len(products_after_filtering), 0)

        # Click on "Chairs" tab to change the filter
        chair_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@data-name='chairs']")))
        chair_tab.click()

        # Verify that product list is updated after applying the new filter
        products_after_filtering = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='col-sm-4 col-xs-6']/div[1]")))
        self.assertGreater(len(products_after_filtering), 0)

        # Click "All" to remove the filter
        all_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, "//li[@data-name='all']")))
        all_tab.click()

        # Confirm that the full list of products is shown after removing the filter
        products_after_removal = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.XPATH, "//div[@class='col-sm-4 col-xs-6']/div[1]")))
        self.assertEqual(len(products_after_removal), len(products_after_filtering))

if __name__ == '__main__':
    unittest.main()