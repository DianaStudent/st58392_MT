import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReactApp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_shop_react_app(self):
        self.driver.get("http://localhost/")

        # Check for navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".nav-link"))
        )
        self.assertEqual(len(nav_links), 4)
        self.assertIn("Tables", [link.text for link in nav_links])

        # Check for inputs and buttons
        inputs_and_buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input, button"))
        )
        self.assertGreater(len(inputs_and_buttons), 0)

        # Interact with the UI (e.g. click a button)
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_button.click()

        # Check for banner
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".toast-toast__container"))
        )

        self.assertEqual(banner.text.strip(), "")

    def test_shop_react_app_tables(self):
        self.driver.get("http://localhost/category/tables")

        # Check for tables link
        tables_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tables"))
        )

        # Interact with the UI (e.g. click the tables link)
        tables_link.click()

if __name__ == "__main__":
    unittest.main()