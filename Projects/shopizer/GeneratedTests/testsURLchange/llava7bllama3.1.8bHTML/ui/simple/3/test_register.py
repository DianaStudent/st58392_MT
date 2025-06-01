import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestShopReact(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_main_ui_components_present(self):
        # Check if header is present
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        self.assertTrue(header.is_displayed())

        # Check if buttons are present
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Check if links are present
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            self.assertTrue(link.is_displayed())

        # Check if form fields are present
        form_fields = self.driver.find_elements(By.NAME, "field")
        for field in form_fields:
            self.assertTrue(field.is_displayed())

    def test_tables_page(self):
        self.driver.get("http://localhost/category/tables")

        # Check if table header is present
        table_header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "th")))
        self.assertTrue(table_header.is_displayed())

        # Check if table rows are present
        table_rows = self.driver.find_elements(By.TAG_NAME, "tr")
        for row in table_rows:
            self.assertTrue(row.is_displayed())

    def test_chairs_page(self):
        self.driver.get("http://localhost/category/chairs")

        # Check if chair header is present
        chair_header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        self.assertTrue(chair_header.is_displayed())

    def test_login_page(self):
        self.driver.get("http://localhost/login")

        # Check if login form is present
        login_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "login-form")))
        self.assertTrue(login_form.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()