from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check Header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        except:
            self.fail("Header is not visible.")

        # Check Logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo-image img[alt='logo']")))
        except:
            self.fail("Logo is not visible.")
        
        # Check Category Links
        try:
            category_a = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            category_b = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            category_c = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))
        except:
            self.fail("Category links are not visible.")

        # Check Search Box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))
        except:
            self.fail("Search box is not visible.")

        # Check Cart Icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button img[alt='cart']")))
        except:
            self.fail("Cart icon is not visible.")

        # Check Slider
        try:
            slider = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".home-slider .image-gallery")))
        except:
            self.fail("Slider is not visible.")
        
        # Check Best Sellers Section
        try:
            best_sellers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4.has-text-centered")))
        except:
            self.fail("Best Sellers section is not visible.")
        
        # Check Footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        except:
            self.fail("Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()