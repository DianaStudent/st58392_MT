from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_home_page_elements(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul > li"))
        )
        for link in navigation_links:
            assert link.is_displayed()

        # Inputs and buttons
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'search')))
        assert search_input.is_displayed()
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        assert add_to_cart_button.is_displayed()

        # Banners
        banner_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'banner')))
        assert banner_element.is_displayed()

    def test_interactive_elements(self):
        search_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.NAME, 'search')))
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        banner_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'banner')))

        # Click a button and check that the UI updates visually
        add_to_cart_button.click()
        WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.ID, 'cart')))
        cart_element = self.driver.find_element(By.ID, 'cart')
        assert cart_element.is_displayed()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()