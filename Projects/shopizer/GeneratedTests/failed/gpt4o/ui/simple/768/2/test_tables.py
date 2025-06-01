from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check for header elements
            header_logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a")))
            header_home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
            header_tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
            header_chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
            
            # Check for account and cart buttons
            account_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))

            # Check for login and register links
            login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
            register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
            
            # Check for product elements
            product_list = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-area")))
            products = product_list.find_elements(By.CLASS_NAME, "product-wrap")
            
            self.assertTrue(len(products) > 0, "No products found on the page.")

            # Check for footer elements
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))

        except Exception as e:
            self.fail(f"An expected element is missing or not visible: {str(e)}")

if __name__ == "__main__":
    unittest.main()