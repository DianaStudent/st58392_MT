import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        # Quit the driver
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver
        
        try:
            # Define selectors
            header_selector = (By.CLASS_NAME, "header-area")
            accept_cookies_button_selector = (By.ID, "rcc-confirm-button")
            main_menu_selector = (By.CSS_SELECTOR, "div.main-menu nav ul")
            language_dropdown_selector = (By.CLASS_NAME, "lang-car-dropdown")
            login_link_selector = (By.LINK_TEXT, "Login")
            register_link_selector = (By.LINK_TEXT, "Register")
            cart_icon_selector = (By.CLASS_NAME, "icon-cart")
            subscribe_form_selector = (By.CSS_SELECTOR, "form input.email")
            subscribe_button_selector = (By.CSS_SELECTOR, "form button.button")

            # Wait and check elements
            WebDriverWait(driver, 20).until(EC.presence_of_element_located(header_selector))
            header = driver.find_element(*header_selector)
            if not header.is_displayed():
                self.fail("Header not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(accept_cookies_button_selector))
            accept_cookies_button = driver.find_element(*accept_cookies_button_selector)
            if not accept_cookies_button.is_displayed():
                self.fail("Accept Cookies button not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(main_menu_selector))
            main_menu = driver.find_element(*main_menu_selector)
            if not main_menu.is_displayed():
                self.fail("Main menu not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(language_dropdown_selector))
            language_dropdown = driver.find_element(*language_dropdown_selector)
            if not language_dropdown.is_displayed():
                self.fail("Language dropdown not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(login_link_selector))
            login_link = driver.find_element(*login_link_selector)
            if not login_link.is_displayed():
                self.fail("Login link not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(register_link_selector))
            register_link = driver.find_element(*register_link_selector)
            if not register_link.is_displayed():
                self.fail("Register link not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(cart_icon_selector))
            cart_icon = driver.find_element(*cart_icon_selector)
            if not cart_icon.is_displayed():
                self.fail("Cart icon not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(subscribe_form_selector))
            subscribe_form = driver.find_element(*subscribe_form_selector)
            if not subscribe_form.is_displayed():
                self.fail("Subscribe form field not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located(subscribe_button_selector))
            subscribe_button = driver.find_element(*subscribe_button_selector)
            if not subscribe_button.is_displayed():
                self.fail("Subscribe button not visible")
        
        except Exception as e:
            self.fail(f"An error occurred: {e}")

if __name__ == "__main__":
    unittest.main()