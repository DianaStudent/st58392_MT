from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestShopUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//header//div[@class='logo']/a/img")))
        except:
            self.fail("Logo is not visible.")
        
        # Check navigation links
        try:
            nav_links = [
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home"))),
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))),
                wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
            ]
        except:
            self.fail("One or more navigation links are not visible.")
        
        # Check login and register links
        try:
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        except:
            self.fail("Login or Register link is not visible.")
        
        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie consent button is not visible.")
        
        # Check product elements
        try:
            product_images = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-img img")))
            product_titles = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-content h3 a")))
            product_prices = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".product-price span")))
        except:
            self.fail("Product elements are not visible.")

        # Assertions to ensure presence of elements expected on the page
        for image, title, price in zip(product_images, product_titles, product_prices):
            self.assertTrue(image.is_displayed(), "Product image is not visible.")
            self.assertTrue(title.is_displayed(), "Product title is not visible.")
            self.assertTrue(price.is_displayed(), "Product price is not visible.")

if __name__ == "__main__":
    unittest.main()