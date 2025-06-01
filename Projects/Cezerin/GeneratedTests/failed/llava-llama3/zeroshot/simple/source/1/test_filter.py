from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class TestFilterProcess(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter_process(self):
        # Go to the URL
        self.driver.get("http://localhost:3000/category-a")

        # Apply and remove the filter
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='brand']")))
        checkbox = self.driver.find_element_by_name('brand')
        self.assertTrue(checkbox.is_selected())
        WebDriverWait(self.driver, 2)
        checkbox.click()
        WebDriverWait(self.driver, 2)

        # Change price filtering
        select_price = self.driver.find_element_by_id('price_filter')
        for i in range(1, 5):
            select_price.select_by_index(str(i))
            self.assertTrue(EC.visibility_of_all_elements_located((By.XPATH, "//div[contains(@class,'product-card')]")))
            WebDriverWait(self.driver, 2)

if __name__ == '__main__':
    unittest.main()