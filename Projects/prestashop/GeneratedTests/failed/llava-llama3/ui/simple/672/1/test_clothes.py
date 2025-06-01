from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

class ClothesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(options=Options(binary="path/to/chromedriver"))
        self.url = "http://localhost:8080/en/3-clothes"
        self.login_url = "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"

    def tearDown(self):
        self.driver.quit()

    def test_clothes(self):
        self.driver.get(self.url)
        self.assertTrue(self.is_element_present("header"))
        self.assertTrue(self.is_element_present("nav"))

        # Select the 'Jackets' subcategory
        jacket_tab = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains('jackets')]")))
        self.assertTrue(self.is_element_present("li[contains('Jackets')]))
        self.assertTrue(self.is_element_present("a[contains('Jackets')]"))

        # Select the 'Black' color
        black_color = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[contains('Black color')]")))
        self.assertTrue(self.is_element_present("a[contains('Black color')]"))
        self.assertTrue(self.is_element_present("li[contains('Jackets')][contains('black color')]"))

    def is_element_present(self, element_name):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//*[contains({element_name})]")))
            return True
        except WebDriverException:
            return False

if __name__ == '__main__':
    unittest.main()