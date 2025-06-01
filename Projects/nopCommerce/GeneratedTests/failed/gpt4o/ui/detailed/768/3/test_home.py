from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.set_window_size(1920, 1080)

    def test_ui_elements(self):
        driver = self.driver

        # Wait and check for header visibility
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header"))
        )
        self.assertIsNotNone(header, "Header is missing.")

        # Check for footer visibility
        footer = driver.find_element(By.CLASS_NAME, "footer")
        self.assertTrue(footer.is_displayed(), "Footer is missing.")

        # Check for navigation menu visibility
        nav_menu = driver.find_element(By.CSS_SELECTOR, "ul.top-menu.notmobile")
        self.assertTrue(nav_menu.is_displayed(), "Navigation menu is missing.")

        # Check for search box visibility
        search_box = driver.find_element(By.ID, "small-search-box-form")
        self.assertTrue(search_box.is_displayed(), "Search box is missing.")

        # Check for register link
        register_link = driver.find_element(By.LINK_TEXT, "Register")
        self.assertTrue(register_link.is_displayed(), "Register link is missing.")

        # Check for login link
        login_link = driver.find_element(By.LINK_TEXT, "Log in")
        self.assertTrue(login_link.is_displayed(), "Login link is missing.")

        # Check for shopping cart link
        cart_link = driver.find_element(By.CSS_SELECTOR, "#topcartlink a.ico-cart")
        self.assertTrue(cart_link.is_displayed(), "Shopping cart link is missing.")

        # Interact with search button
        search_button = search_box.find_element(By.CSS_SELECTOR, "button.search-box-button")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-box-button"))).click()
        self.assertTrue(search_button.is_displayed(), "Search button is missing or not interactive.")

        # Check the newsletter subscription button
        subscribe_button = driver.find_element(By.ID, "newsletter-subscribe-button")
        self.assertTrue(subscribe_button.is_displayed(), "Newsletter Subscribe button is missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()