import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestShopUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_home_page(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.failUnlessElementPresent(self.driver.find_element(By.TAG_NAME, "h1"), 'Header')
        self.failUnlessElementVisible(self.driver.find_element(By.TAG_NAME, "h1"))

    def test_tables_page(self):
        self.driver.get("http://localhost/category/tables")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Chairs")))
        self.failUnlessElementPresent(self.driver.find_element(By.LINK_TEXT, "Chairs"), 'Link to chairs')
        self.failUnlessElementVisible(self.driver.find_element(By.LINK_TEXT, "Chairs"))

    def test_chairs_page(self):
        self.driver.get("http://localhost/category/chairs")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Tables")))
        self.failUnlessElementPresent(self.driver.find_element(By.LINK_TEXT, "Tables"), 'Link to tables')
        self.failUnlessElementVisible(self.driver.find_element(By.LINK_TEXT, "Tables"))

    def test_login_page(self):
        self.driver.get("http://localhost/login")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        self.failUnlessElementPresent(self.driver.find_element(By.NAME, "username"), 'Username input')
        self.failUnlessElementVisible(self.driver.find_element(By.NAME, "username"))

    def test_register_page(self):
        self.driver.get("http://localhost/register")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        self.failUnlessElementPresent(self.driver.find_element(By.NAME, "username"), 'Username input')
        self.failUnlessElementVisible(self.driver.find_element(By.NAME, "username"))

    def failUnlessElementPresent(self, element, message):
        if not element:
            self.fail(f'Element "{message}" is missing')

    def failUnlessElementVisible(self, element, message):
        if not element.is_displayed():
            self.fail(f'Element "{message}" is not visible')

if __name__ == '__main__':
    unittest.main()