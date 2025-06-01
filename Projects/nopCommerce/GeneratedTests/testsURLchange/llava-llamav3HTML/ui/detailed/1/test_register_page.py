import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

class MaxTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        self.driver.get("http://max/")
        elements_to_check = ["header", "footer", "header"]
        for element in elements_to_check:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//*[name='{element}']/div")))
            self.assertTrue(self.driver.page_source.count(element))

    def test_login_page(self):
        self.driver.get("http://max/login?returnUrl=%2F")
        elements_to_check = ["login_username", "password"]
        for element in elements_to_check:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//*[name='{element}']/input")))
            self.assertTrue(self.driver.page_source.count(element))

    def test_register_page(self):
        self.driver.get("http://max/register?returnUrl=%2F")
        elements_to_check = ["email", "password"]
        for element in elements_to_check:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//*[name='{element}']/input")))
            self.assertTrue(self.driver.page_source.count(element))

    def test_search_page(self):
        self.driver.get("http://max/search")
        elements_to_check = ["search_box"]
        for element in elements_to_check:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, f"//*[name='{element}']/input")))
            self.assertTrue(self.driver.page_source.count(element))

if __name__ == '__main__':
    unittest.main()