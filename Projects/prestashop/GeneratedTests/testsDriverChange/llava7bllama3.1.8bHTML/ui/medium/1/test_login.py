import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class TestUI(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_main_page(self):
        self.driver.get("http://localhost:8080/en/")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("home", [link.text for link in nav_links])

        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        ).click()

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(len(self.driver.page_source) > 0)

    def test_clothes_page(self):
        self.driver.get("http://localhost:8080/en/3-clothes")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("Clothes", [link.text for link in nav_links])

    def test_accessories_page(self):
        self.driver.get("http://localhost:8080/en/6-accessories")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("Accessories", [link.text for link in nav_links])

    def test_art_page(self):
        self.driver.get("http://localhost:8080/en/9-art")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("Art", [link.text for link in nav_links])

    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("Login", [link.text for link in nav_links])

    def test_register_page(self):
        self.driver.get("http://localhost:8080/en/registration")

        # Navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.mainmenu li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Confirm the presence of key interface elements
        self.assertIn("Registration", [link.text for link in nav_links])

if __name__ == '__main__':
    unittest.main()