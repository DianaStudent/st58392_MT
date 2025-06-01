import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopifyLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_load_page(self):
        self.driver.get("http://localhost/")
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//header//h1[contains(text(), 'Shopify')]")))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//header//a[contains(@href, 'category/tables')]"))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//header//a[contains(@href, 'category/chairs')]"))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//div[contains(text(), 'Sign in or')]")))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//form[contains(@id, 'login-form')]"))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//input[contains(@name, 'email')]"))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//input[contains(@name, 'password')]"))
        self.assertTrue(EC.presence_of_elements_located((By.XPATH, "//button[contains(text(), 'Log in')]"))))

if __name__ == '__main__':
    unittest.main()