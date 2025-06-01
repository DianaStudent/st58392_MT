import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestECommerceUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_homepage_elements(self):
        # Go to homepage
        self.driver.get("http://localhost/")

        # Wait for page to load and check main elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check that header exists and is visible
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertTrue(header.is_displayed())

        # Check that navigation menu exists and contains expected items
        nav_menu = self.driver.find_elements(By.XPATH, "//nav//a")
        self.assertEqual(len(nav_menu), 9)
        self.assertIn("Home", [item.text for item in nav_menu])
        self.assertIn("Men", [item.text for item in nav_menu])
        self.assertIn("Women", [item.text for item in nav_menu])
        self.assertIn("Kids", [item.text for item in nav_menu])

    def test_tables_page_elements(self):
        # Go to tables page
        self.driver.get("http://localhost/category/tables")

        # Wait for page to load and check main elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check that header exists and is visible
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertTrue(header.is_displayed())

        # Check that product list exists and contains expected number of items
        products = self.driver.find_elements(By.XPATH, "//div[@class='product']")

        self.assertGreater(len(products), 0)

    def test_chairs_page_elements(self):
        # Go to chairs page
        self.driver.get("http://localhost/category/chairs")

        # Wait for page to load and check main elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check that header exists and is visible
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertTrue(header.is_displayed())

        # Check that product list exists and contains expected number of items
        products = self.driver.find_elements(By.XPATH, "//div[@class='product']")

        self.assertGreater(len(products), 0)

    def test_login_page_elements(self):
        # Go to login page
        self.driver.get("http://localhost/login")

        # Wait for page to load and check main elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check that header exists and is visible
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertTrue(header.is_displayed())

        # Check that form fields exist
        form_fields = self.driver.find_elements(By.XPATH, "//form//input")

        self.assertGreater(len(form_fields), 0)

    def test_register_page_elements(self):
        # Go to register page
        self.driver.get("http://localhost/register")

        # Wait for page to load and check main elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check that header exists and is visible
        header = self.driver.find_element(By.XPATH, "//h1")
        self.assertTrue(header.is_displayed())

        # Check that form fields exist
        form_fields = self.driver.find_elements(By.XPATH, "//form//input")

        self.assertGreater(len(form_fields), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()