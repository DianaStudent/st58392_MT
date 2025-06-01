import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestWebPageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify structural elements
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertIsNotNone(header, "Header not found or not visible")

        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertIsNotNone(footer, "Footer not found or not visible")

        # Verify top menu
        menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
        self.assertIsNotNone(menu, "Top menu not found or not visible")

        # Verify search box
        search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
        self.assertIsNotNone(search_box, "Search box not found or not visible")

        # Verify register and login links
        register_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.ico-register')))
        self.assertIsNotNone(register_link, "Register link not found or not visible")

        login_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.ico-login')))
        self.assertIsNotNone(login_link, "Login link not found or not visible")

        # Verify shopping cart link
        cart_link = wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
        self.assertIsNotNone(cart_link, "Cart link not found or not visible")

        # Verify search functionality
        search_input = driver.find_element(By.ID, 'small-searchterms')
        search_button = driver.find_element(By.CLASS_NAME, 'search-box-button')
        search_input.send_keys('test')
        search_button.click()
        
        # Simulate waiting for search results to be be visible

        # Verify slider
        slider = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'swiper-nop-slider')))
        self.assertIsNotNone(slider, "Slider not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()