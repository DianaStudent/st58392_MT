import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApp(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_main_ui_components(self):
        self.driver.get("http://localhost/")

        # Check if main header is present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertIsNotNone(header)
        self.assertTrue(header.is_displayed())

        # Check if buttons are present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.assertIsNotNone(button)
        self.assertTrue(button.is_displayed())

        # Check if links are present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
        link = self.driver.find_element(By.XPATH, "//a[@href='/category/tables']")
        self.assertIsNotNone(link)
        self.assertTrue(link.is_displayed())

        # Check if form fields are present and visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@type='email']")))
        email_field = self.driver.find_element(By.XPATH, "//input[@type='email']")
        self.assertIsNotNone(email_field)
        self.assertTrue(email_field.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()