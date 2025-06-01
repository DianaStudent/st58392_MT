import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_ui_elements(self):
        driver = self.driver
    
        # Check Header visibility
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible.")
        
        # Check Footer visibility
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")
        
        # Check Navigation visibility
        nav = driver.find_elements(By.CSS_SELECTOR, '.primary-nav ul.nav-level-0 li')
        self.assertTrue(len(nav) > 0, "Navigation bar is not visible or empty.")
        
        # Check Search Box
        search_box = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        
        # Check Search Input
        search_input = search_box.find_element(By.CLASS_NAME, 'search-input')
        self.assertTrue(search_input.is_displayed(), "Search input is not visible.")
        
        # Click Search Icon
        search_icon = search_box.find_element(By.CLASS_NAME, 'search-icon-search')
        self.wait.until(EC.element_to_be_clickable(search_icon)).click()
        
        # Check Category Links
        category_links = driver.find_elements(By.CSS_SELECTOR, '.nav-level-0 a')
        self.assertTrue(len(category_links) > 0, "Category links are not visible or missing.")

        # Check slider images
        slider_images = driver.find_elements(By.CSS_SELECTOR, '.home-slider .image-gallery-image img')
        self.assertTrue(len(slider_images) > 0, "Slider images are not visible.")
        
        # Check Best Sellers section
        best_sellers_section = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".title.is-4")))
        self.assertTrue(best_sellers_section.is_displayed() and best_sellers_section.text == "BEST SELLERS", "Best Sellers section is not visible or incorrect.")
        
        # Check Product Links
        product_links = driver.find_elements(By.CSS_SELECTOR, '.content.product-caption .product-name')
        self.assertTrue(len(product_links) > 0, "Product links are not visible or missing.")

        # Check Cart Button
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible.")
        
        # Click Cart Button
        cart_button.click()

        # Check mini-cart visibility
        mini_cart = self.wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'mini-cart')))
        self.assertTrue(len(mini_cart) > 0, "Mini cart is not visible.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()