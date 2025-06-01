import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import ExpectedConditions
from selenium.webdriver.common.utils import _is_split_location_path

class TestClothes(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost:8080/en/"
    
    def tearDown(self):
        self.driver.quit()

    def test_clothes_page(self):
        driver = self.driver
        driver.get(self.base_url + "clothes")
        
        # Confirm the presence of key interface elements
        assert WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'CLOTHES')]")))
        )
        assert WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']"))
        )
        
        # Interact with elements
        select = Select(driver.find_element_by_xpath("//select[@name='category']"))
        select.select_by_index(1)
        button = driver.find_element_by_name("submit")
        button.click()
        
        # Verify that interactive elements do not cause errors in the UI
        assert WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Clothes')]"))
        )
        assert WebDriverWait(driver, 20).until(
            EC.presence_of_element_search("iframe", {"src": "//localhost:8080/en/3-clothes"})
        )

if __name__ == '__main__':
    unittest.main()