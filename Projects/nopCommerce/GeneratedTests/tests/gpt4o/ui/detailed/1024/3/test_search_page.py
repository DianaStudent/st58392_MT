import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/search')

    def test_ui_elements(self):
        driver = self.driver

        # Wait for elements to be visible
        def is_element_visible(locator):
            try:
                return WebDriverWait(driver, 20).until(EC.visibility_of_element_located(locator))
            except:
                return False

        # Check the visibility of header, footer, and navigation elements
        header = is_element_visible((By.CLASS_NAME, 'header'))
        footer = is_element_visible((By.CLASS_NAME, 'footer'))
        nav = is_element_visible((By.CLASS_NAME, 'header-menu'))
        
        # Check the visibility of key UI elements
        search_input = is_element_visible((By.ID, 'small-searchterms'))
        search_button = is_element_visible((By.CLASS_NAME, 'search-box-button'))
        register_link = is_element_visible((By.CLASS_NAME, 'ico-register'))
        login_link = is_element_visible((By.CLASS_NAME, 'ico-login'))
        cart_link = is_element_visible((By.CLASS_NAME, 'ico-cart'))
        wishlist_link = is_element_visible((By.CLASS_NAME, 'ico-wishlist'))
        search_label = is_element_visible((By.XPATH, "//label[@for='q']"))
        advanced_search_checkbox = is_element_visible((By.ID, 'advs'))
        
        # Ensure all elements are visible
        if not all([header, footer, nav, search_input, search_button, register_link, 
                    login_link, cart_link, wishlist_link, search_label, advanced_search_checkbox]):
            self.fail("One or more required UI elements are not visible.")

        # Interact with elements
        search_input_box = driver.find_element(By.ID, 'small-searchterms')
        search_input_box.send_keys('book')
        search_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()