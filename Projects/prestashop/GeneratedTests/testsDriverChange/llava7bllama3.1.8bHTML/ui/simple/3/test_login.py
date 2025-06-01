import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestECommerceSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components_are_present(self):
        # Check header is present
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.failUnless(header.is_displayed())

        # Check buttons are present
        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button"))
        )
        for button in buttons:
            self.failUnless(button.is_displayed())

        # Check links are present
        links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )
        for link in links:
            self.failUnless(link.is_displayed())

        # Check form fields are present
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.NAME, "email"))
        )
        for field in form_fields:
            self.failUnless(field.is_displayed())

    def test_clothes_category_is_present(self):
        self.driver.get("http://localhost:8080/en/3-clothes")
        clothes_category = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.failUnless(clothes_category.is_displayed())

    def test_accessories_category_is_present(self):
        self.driver.get("http://localhost:8080/en/6-accessories")
        accessories_category = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.failUnless(accessories_category.is_displayed())

    def test_art_category_is_present(self):
        self.driver.get("http://localhost:8080/en/9-art")
        art_category = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.failUnless(art_category.is_displayed())

    def test_login_page_is_present(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")
        login_page = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        self.failUnless(login_page.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()