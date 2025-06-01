from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8,{html}".format(html=html_data["html"]))

    def test_ui_components_exist(self):
        driver = self.driver
        
        try:
            # Check for header existence and visibility
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'header'))
            )
            
            # Check for logo existence and visibility
            logo = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image img'))
            )
            
            # Check for search box existence and visibility
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input'))
            )
            
            # Check for cart icon existence and visibility
            cart_icon = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.cart-button img'))
            )
            
            # Check for primary navigation existence and visibility
            primary_nav = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.primary-nav'))
            )
            
            # Check for mobile navigation existence and visibility
            mobile_nav = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.mobile-nav'))
            )
            
            # Check for subcategory link existence and visibility
            subcategory_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']"))
            )
            
            # Check for filter button existence and visibility in mobile view
            filter_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button.is-fullwidth"))
            )
            
            # Check for product link existence and visibility
            product_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            
            # Check for footer existence and visibility
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
            )

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()