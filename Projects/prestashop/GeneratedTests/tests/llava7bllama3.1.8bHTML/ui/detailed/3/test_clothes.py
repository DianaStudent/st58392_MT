import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestArtShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/9-art")

    def test_art_shop_page_loads_properly(self):
        # Header is visible and present
        header_element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//header"))
        )
        self.assertTrue(header_element.is_displayed())

        # Main content area is visible and present
        main_content_area = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//main"))
        )
        self.assertTrue(main_content_area.is_displayed())

        # Header elements are present and clickable
        header_elements = [
            ("//a[@href='/en/']", "Home"),
            ("//a[@href='/en/3-clothes']", "Clothes"),
            ("//a[@href='/en/6-accessories']", "Accessories")
        ]
        for xpath, text in header_elements:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.assertTrue(element.is_enabled())
            element.click()
            self.assertEqual(text, WebDriverWait(self.driver, 10).until(EC.title_contains).strip())

        # Registration and login links are present
        registration_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        self.assertTrue(registration_link.is_enabled())
        registration_link.click()
        self.assertEqual("Registration | Art Shop", WebDriverWait(self.driver, 10).until(EC.title_contains).strip())

        login_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        self.assertTrue(login_link.is_enabled())
        login_link.click()
        self.assertEqual("Login | Art Shop", WebDriverWait(self.driver, 10).until(EC.title_contains).strip())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()