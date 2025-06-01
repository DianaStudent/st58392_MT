from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilters(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")  # assuming your application is running on this URL

    def tearDown(self):
        self.driver.quit()

    def test_filter_tab(self):
        try:
            filter_tab = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='filter']"))
            )
            filter_tab.click()
        except TimeoutException:
            self.fail("Timeout waiting for filter tab to be clickable")
        except NoSuchElementException:
            self.fail("Filter tab not found")

        # wait for products to load
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product']"))
        )

        initial_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product']"))

        # apply filter (assuming this button is inside the filter tab)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='apply-filter-btn']"))
        ).click()

        final_product_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product']))

        # check that at least one product is displayed after applying filters
        self.assertGreater(final_product_count, 0)

        # check that the number of products has changed after applying filters
        self.assertNotEqual(initial_product_count, final_product_count)

if __name__ == "__main__":
    unittest.main()