import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestMax(unittest.TestCase):

    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max/")

    def test_max_elements_present(self):
        # Home page elements
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//h1[contains(text(), 'Max')]")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-form")))

        # Search form fields
        search_input = self.driver.find_element(By.NAME, "search")
        self.assertIsNotNone(search_input)
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        self.assertIsNotNone(search_button)

        # Login page elements
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Login')]")))
        self.assertIsNotNone(login_link)
        login_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-form")))

        # Register page elements
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Register')]")))
        self.assertIsNotNone(register_link)
        register_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-form")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()