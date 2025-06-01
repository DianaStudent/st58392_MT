from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_max_website(self):
        # 1. Open the page.
        self.driver.get("http://max/")

        # 2. Confirm the presence of key interface elements:
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#nav > li:nth-child(1) > a"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "search_query_top"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "submit_search"))
            )
        except TimeoutException:
            self.fail("Missing required elements")

        # 3. Interact with one or two elements
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "submit_search"))
        )
        search_button.click()

        # Check that the UI updates visually
        self.assertTrue(search_button.get_attribute("class") != "")

    def test_max_login_page(self):
        # Login page
        self.driver.get("http://max/login?returnUrl=%2F")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "SubmitLogin"))
            )
        except TimeoutException:
            self.fail("Missing required elements")

    def test_max_register_page(self):
        # Register page
        self.driver.get("http://max/register?returnUrl=%2F")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "SubmitCreate"))
            )
        except TimeoutException:
            self.fail("Missing required elements")

    def test_max_search_page(self):
        # Search page
        self.driver.get("http://max/search")

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.ID, "search_query_top"))
            )
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "submit_search"))
            )
        except TimeoutException:
            self.fail("Missing required elements")


if __name__ == '__main__':
    unittest.main()