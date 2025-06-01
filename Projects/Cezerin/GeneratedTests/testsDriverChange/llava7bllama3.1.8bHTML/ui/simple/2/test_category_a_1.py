import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestHomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def setUp(self):
        self.driver.get("http://example.com")  # Replace with your URL

    def test_main_ui_components_present(self):
        try:
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//header"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-header__title']"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category_a/category_a_1']"))
            )
        except:
            self.fail("Required elements are missing")

    def test_main_ui_components_visible(self):
        try:
            header = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//header"))
            )
            self.assertTrue(header.is_displayed())
            h1_title = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-header__title']"))
            )
            self.assertTrue(h1_title.is_displayed())
            button = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))
            )
            self.assertTrue(button.is_displayed())
            link = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category_a/category_a_1']"))
            )
            self.assertTrue(link.is_displayed())
        except:
            self.fail("Required elements are missing")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()