```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_filter(self):
        # Open the home page
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        # Click on the "Art" category in the top menu
        art_category = driver.find_element_by_xpath("//*[name='a' and @id='header']/span[contains(text(), 'Art')]")
        art_category.click()
        
        # Wait for the category page to load
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,
                                                                 "//*[name='section' and @class='filter-section']/div[contains(@data-name, 'Matt paper')]")))
        
        # Select a checkbox filter. Use label or section attributes like data-name instead.
        matt_paper_filter = driver.find_element_by_xpath("//*[name='label' and @for='Matt paper']")
        matt_paper_filter.click()
        
        # Wait for the filters to take effect
        WebDriverWait(driver, 20).until(EC.change_element_count("//*[name='div' and @class='product-tile']"), 10)
        
        # Assert that the number of product tiles is reduced from 7 to 3
        self.assertEqual(len(driver.find_elements_by_xpath("//*[name='div' and @class='product-tile']")), 3)
        
        # Locate and click the "Clear all" button to remove filters
        clear_button = driver.find_element_by_name("clearButton")
        ActionChains().move_to_element(clear_button).click().perform()
        
        # Wait for the number of products to return to the original count
        WebDriverWait(driver, 20).until(EC.change_element_count("//*[name='div' and @class='product-tile']"), 10)
        
        self.assertEqual(len(driver.find_elements_by_xpath("//*[name='div' and @class='product-tile']")), 7)

if __name__ == "__main__":
    unittest.main()
```