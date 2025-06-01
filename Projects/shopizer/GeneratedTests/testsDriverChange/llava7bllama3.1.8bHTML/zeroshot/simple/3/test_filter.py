import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilterTab(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_filter_tab(self):
        # Open the webpage
        self.driver.get("http://localhost/")

        # Click on the filter tab
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/filter']"))).click()

        # Check that at least one product is displayed after applying filters
        try:
            self.assertGreater(len(WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='product-list']//li")))), 0)
        except AssertionError:
            self.fail("No products are displayed after applying filters")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()