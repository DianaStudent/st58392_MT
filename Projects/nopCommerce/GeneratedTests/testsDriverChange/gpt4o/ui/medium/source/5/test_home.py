import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check the presence and visibility of the logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header-logo a img")))
        except:
            self.fail("Logo is not visible")

        # Check the presence and visibility of the navigation links
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-menu .top-menu.notmobile")))
        except:
            self.fail("Navigation links are not visible")
        
        # Check the presence and visibility of the search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
        except:
            self.fail("Search box is not visible")
        
        # Check the presence and visibility of the banners
        try:
            banners = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".swiper.nop-slider")))
        except:
            self.fail("Banners are not visible")

        # Interact with the search box (e.g., input text and ensure no errors)
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_input.send_keys("test")
            search_button = driver.find_element(By.CSS_SELECTOR, "button.search-box-button")
            search_button.click()
            wait.until(EC.url_contains("search?q=test"))
        except:
            self.fail("Search functionality is not working as expected")
        
        # Check the presence and visibility of footer links
        try:
            footer_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer-lower .footer-info")))
        except:
            self.fail("Footer links are not visible")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()