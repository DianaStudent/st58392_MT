from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        
    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://max/")

        try:
            # Wait for the header to be visible
            header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertIsNotNone(header, "Header should be present")

            # Check for navigation menu
            nav_menu = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertIsNotNone(nav_menu, "Navigation menu should be present")

            # Check for search box
            search_box = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            self.assertIsNotNone(search_box, "Search box should be present")

            # Check for footer
            footer = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertIsNotNone(footer, "Footer should be present")

            # Check for search button and click it
            search_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            search_button.click()

            # Check for 'Register' link
            register_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.assertTrue(register_link.is_displayed(), "Register link should be visible")

            # Check for 'Log in' link
            login_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.assertTrue(login_link.is_displayed(), "Log in link should be visible")

            # Check for 'Shopping cart' link
            cart_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
            self.assertTrue(cart_link.is_displayed(), "Shopping cart link should be visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()