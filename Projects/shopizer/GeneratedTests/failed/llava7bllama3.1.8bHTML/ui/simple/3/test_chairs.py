from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        # Headers
        header_title = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1"))
        )
        self.failUnless(header_title.is_displayed(), "Header title is not visible")
        
        header_logout = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/login/logout']"))
        )
        self.failUnless(header_logout.is_displayed(), "Logout link is not visible")

        # Buttons
        button_search = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search-button']"))
        )
        self.failUnless(button_search.is_enabled(), "Search button is not enabled")
        
        button_cart = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))
        )
        self.failUnless(button_cart.is_displayed(), "Cart button is not visible")

        # Links
        link_tables = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category/tables']"))
        )
        self.failUnless(link_tables.is_enabled(), "Tables link is not enabled")
        
        link_chairs = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/category/chairs']"))
        )
        self.failUnless(link_chairs.is_displayed(), "Chairs link is not visible")

        # Form fields
        field_username = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='username']"))
        )
        self.failUnless(field_username.is_enabled(), "Username field is not enabled")
        
        field_password = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        )
        self.failUnless(field_password.is_displayed(), "Password field is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()