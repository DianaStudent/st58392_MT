```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class TestEcomWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        self.assertTrue("header" in driver.page_source)
        self.assertTrue("footer" in driver.page_source)

    def test_check_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/3-clothes")
        self.assertTrue("h2" in driver.page_source)
        self.assertTrue(".image" in driver.page_source)
        self.assertTrue(".price" in driver.page_source)
        self.assertTrue(".name" in driver.page_source)

    def test_interact_with_key_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/3-clothes")
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h2"))
        )
        text = "T-shirt"
        text_input = WebDriverWait(header, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[contains(@name,'text')]")))
        self.assertEqual(text, text_input.get_attribute("value"))

if __name__ == '__main__':
    unittest.main()
```