from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header elements
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        if not header:
            self.fail("Header is missing.")

        # Check footer elements
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        if not footer:
            self.fail("Footer is missing.")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, ".main-menu nav ul li a")
        if not nav_links:
            self.fail("Navigation links are missing.")
        
        # Check cookie consent button
        cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        if cookie_button:
            cookie_button.click()
        else:
            self.fail("Cookie consent button is missing.")

        # Check presence of input fields in subscribe section
        subscribe_email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 input[name='email']")))
        subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 button.button")))
        if not subscribe_email_input or not subscribe_button:
            self.fail("Subscribe email input or button is missing.")

        # Check presence and interaction with product items
        product_wrap = driver.find_elements(By.CSS_SELECTOR, ".product-wrap-2")
        if not product_wrap:
            self.fail("Product items are missing.")
        for product in product_wrap:
            add_to_cart_button = product.find_element(By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")
            if add_to_cart_button:
                ActionChains(driver).move_to_element(product).click(add_to_cart_button).perform()
            else:
                self.fail("Add to Cart button is missing.")

        # Check login and register links
        account_links = driver.find_elements(By.CSS_SELECTOR, ".account-dropdown ul li a")
        if not account_links:
            self.fail("Login/Register links are missing.")
        else:
            for link in account_links:
                self.assertNotEqual(link.get_attribute('href'), '', "Account link is missing href attribute.")

if __name__ == "__main__":
    unittest.main()