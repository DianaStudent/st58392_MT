import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_process(self):
        self.driver.get('http://localhost/')

        for i in range(5):
            product_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f'//*[@id="product-{i}"]')))
            add_to_cart_button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH,