import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os

class TestEcommerceSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        self.failUnlessElementVisible("//div[@class='react-toast-notifications__container css-1oqa81j']")

    def test_tables_link(self):
        # Click on tables link and check that the page title contains 'tables'
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Tables']")))
        self.driver.find_element(By.XPATH, "//a[text()='Tables']").click()
        WebDriverWait(self.driver, 20).until(EC.title_contains('tables'))

    def test_chairs_link(self):
        # Click on chairs link and check that the page title contains 'chairs'
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Chairs']")))
        self.driver.find_element(By.XPATH, "//a[text()='Chairs']").click()
        WebDriverWait(self.driver, 20).until(EC.title_contains('chairs'))

    def test_login_link(self):
        # Click on login link and check that the URL contains 'login'
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
        self.driver.find_element(By.XPATH, "//a[text()='Login']").click()
        WebDriverWait(self.driver, 20).until(lambda driver: 'login' in self.driver.current_url)

    def test_register_link(self):
        # Click on register link and check that the URL contains 'register'
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Register']")))
        self.driver.find_element(By.XPATH, "//a[text()='Register']").click()
        WebDriverWait(self.driver, 20).until(lambda driver: 'register' in self.driver.current_url)

    def failUnlessElementVisible(self, locator):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            self.fail(f"Expected element to be visible at {locator}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()