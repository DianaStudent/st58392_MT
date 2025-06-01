```
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.time import TimeOuts
from selenium.webdriver.support.assertions import Assert
from selenium.webdriver.common.action_chains import ActionChains

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header[@role='banner']")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='search']")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_clothes_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/3-")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(translate('Clothes'))]")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_accessories_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/6-")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(translate('Accessories'))]")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_art_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/9-")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2[contains(translate('Art'))]")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))

    def test_login_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(translate('Login'))]")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))

    def test_register_page(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/registration")
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(translate('Register'))]")))
        assert WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))

if __name__ == '__main__':
    unittest.main()
```