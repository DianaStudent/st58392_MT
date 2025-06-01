from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Verify header
        header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        if not header:
            self.fail("Header is not present or visible")

        # Verify main navigation links
        main_nav_links = [
            (By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']"),
            (By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']"),
            (By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")
        ]
        for link in main_nav_links:
            element = self.wait.until(EC.visibility_of_element_located(link))
            if not element:
                self.fail(f"Main navigation link {link[1]} is not present or visible")

        # Verify carousel
        carousel = self.wait.until(EC.visibility_of_element_located((By.ID, "carousel")))
        if not carousel:
            self.fail("Carousel is not present or visible")

        # Verify products are displayed
        products_section = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products")))
        if not products_section:
            self.fail("Products section is not present or visible")

        # Verify login and register links
        login_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        if not login_link or not register_link:
            self.fail("Login or register link is not present or visible")

        # Verify search widget
        search_widget = self.wait.until(EC.visibility_of_element_located((By.ID, "search_widget")))
        if not search_widget:
            self.fail("Search widget is not present or visible")

if __name__ == "__main__":
    unittest.main()