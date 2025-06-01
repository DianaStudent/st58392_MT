import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestShopUi(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def tearDown(self):
        self.driver.quit()

    def test_shop_ui(self):
        # Go to the home page
        self.driver.get("http://localhost/")

        # Check presence of key interface elements
        expected_elements = [
            (By.ID, "nav-link-home"),
            (By.ID, "nav-link-tables"),
            (By.ID, "nav-link-chairs"),
            (By.ID, "login-button"),
            (By.ID, "register-button")
        ]

        for selector in expected_elements:
            try:
                WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(selector))
            except TimeoutException:
                self.fail(f"Element {selector} is missing")

        # Interact with the home page
        header_text = (By.XPATH, "//h1[@class='display-4']")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(header_text))
        except TimeoutException:
            self.fail(f"Header element is missing")
        header = self.driver.find_element(*header_text)
        self.assertEqual("Welcome to Shop", header.text)

        # Interact with the tables link
        tables_link = (By.LINK_TEXT, "Tables")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(tables_link))
        except TimeoutException:
            self.fail(f"Link 'Tables' is missing")
        tables_link_element = self.driver.find_element(*tables_link)
        tables_link_element.click()

        # Check that the UI updates visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='display-4']")))
        header_text_tables_page = (By.XPATH, "//h1[@class='display-4']")
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(header_text_tables_page))
        except TimeoutException:
            self.fail(f"Header element is missing on tables page")
        header_tables_page = self.driver.find_element(*header_text_tables_page)
        self.assertEqual("Tables", header_tables_page.text)

if __name__ == "__main__":
    unittest.main()