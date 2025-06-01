import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestNewBalanceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_main_ui_components_present(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".nav-bar")))

        header = self.driver.find_element(By.CSS_SELECTOR, "header")
        nav_bar = self.driver.find_elements(By.CSS_SELECTOR, ".nav-bar")

        self.assertIsNotNone(header)
        for item in nav_bar:
            self.assertIsNotNone(item)

    def test_category_a_url(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "CATEGORY A")))
        category_a_link = self.driver.find_element(By.LINK_TEXT, "CATEGORY A")
        category_a_link.click()

        WebDriverWait(self.driver, 20).until(EC.url_to_be("http://localhost:3000/category-a"))
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost:3000/category-a")

    def test_category_a_1_url(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "CATEGORY A 1")))
        category_a_link = self.driver.find_element(By.LINK_TEXT, "CATEGORY A")
        category_a_link.click()

        category_a_1_link = self.driver.find_element(By.LINK_TEXT, "CATEGORY A 1")
        category_a_1_link.click()

        WebDriverWait(self.driver, 20).until(EC.url_to_be("http://localhost:3000/category-a-1"))
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost:3000/category-a-1")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()