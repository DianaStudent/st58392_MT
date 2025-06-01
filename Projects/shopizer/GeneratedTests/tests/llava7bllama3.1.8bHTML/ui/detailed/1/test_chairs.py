from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestShopReactApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    # Test that structural elements are visible
    def test_structural_elements_visible(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//nav")))

    # Test that input fields and buttons are present
    def test_input_fields_buttons_present(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "search")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "button")))

    # Test that login and register links are present
    def test_login_register_links_present(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='login']")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='register']")))

    # Test that tables page has required elements
    def test_tables_page_elements_present(self):
        self.driver.get("http://localhost/category/tables")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table")))

    # Test that login page has required elements
    def test_login_page_elements_present(self):
        self.driver.get("http://localhost/login")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password")))

    # Test that register page has required elements
    def test_register_page_elements_present(self):
        self.driver.get("http://localhost/register")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "email")))

    # Test that clicking a button reacts visually
    def test_button_click_reaction(self):
        self.driver.get("http://localhost/")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "//p[@class='alert']")))

if __name__ == "__main__":
    unittest.main()