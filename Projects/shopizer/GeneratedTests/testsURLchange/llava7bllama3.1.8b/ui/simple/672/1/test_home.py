import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShopzier(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='logo']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-input")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link")))

        # Check that these elements exist and are visible
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='logo']"))))
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-input"))))

    def test_tables_page_ui_components(self):
        self.driver.get('http://localhost/category/tables')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card")))

    def test_chairs_page_ui_components(self):
        self.driver.get('http://localhost/category/chairs')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-card")))

    def test_login_page_ui_components(self):
        self.driver.get('http://localhost/login')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "password")))

    def test_register_page_ui_components(self):
        self.driver.get('http://localhost/register')
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "username")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))


if __name__ == '__main__':
    unittest.main()