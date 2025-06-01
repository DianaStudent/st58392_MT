from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://max/"

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver
        driver.get(self.base_url)

        # Elements to check on the homepage
        elements_home = {
            "register_link": (By.CSS_SELECTOR, "a.ico-register"),
            "login_link": (By.CSS_SELECTOR, "a.ico-login"),
            "wishlist_link": (By.CSS_SELECTOR, "a.ico-wishlist"),
            "cart_link": (By.CSS_SELECTOR, "a.ico-cart"),
            "search_field": (By.ID, "small-searchterms"),
            "search_button": (By.CSS_SELECTOR, "button.search-box-button"),
            "menu_toggle": (By.CSS_SELECTOR, ".menu-toggle"),
        }

        for element_name, selector in elements_home.items():
            with self.subTest(element=element_name):
                try:
                    element = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located(selector)
                    )
                except:
                    self.fail(f"{element_name} is not visible on home page.")
        
        # Navigate to register page
        driver.get(self.base_url + "register?returnUrl=%2F")

        # Elements to check on the register page
        elements_register = {
            "first_name": (By.ID, "FirstName"),
            "last_name": (By.ID, "LastName"),
            "email": (By.ID, "Email"),
            "password": (By.ID, "Password"),
            "confirm_password": (By.ID, "ConfirmPassword"),
            "register_button": (By.ID, "register-button"),
        }

        for element_name, selector in elements_register.items():
            with self.subTest(element=element_name):
                try:
                    element = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located(selector)
                    )
                except:
                    self.fail(f"{element_name} is not visible on register page.")
        
        # Navigate to login page
        driver.get(self.base_url + "login?returnUrl=%2F")

        # Elements to check on the login page
        elements_login = {
            "login_button": (By.CSS_SELECTOR, "a.ico-login")
        }

        for element_name, selector in elements_login.items():
            with self.subTest(element=element_name):
                try:
                    element = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located(selector)
                    )
                except:
                    self.fail(f"{element_name} is not visible on login page.")
        
        # Navigate to search page
        driver.get(self.base_url + "search")

        # Elements to check on the search page
        elements_search = {
            "search_field": (By.ID, "small-searchterms"),
            "search_button": (By.CSS_SELECTOR, "button.search-box-button"),
        }

        for element_name, selector in elements_search.items():
            with self.subTest(element=element_name):
                try:
                    element = WebDriverWait(driver, 20).until(
                        EC.visibility_of_element_located(selector)
                    )
                except:
                    self.fail(f"{element_name} is not visible on search page.")

if __name__ == "__main__":
    unittest.main()