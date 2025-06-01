import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the page
        driver.get("http://localhost/")

        # 2. Confirm the presence of key interface elements
        try:
            # Checking for presence of navigation links
            home_link = driver.find_element(By.XPATH, "//a[@href='/']")
            wait.until(EC.visibility_of(home_link))

            tables_link = driver.find_element(By.XPATH, "//a[@href='/category/tables']")
            wait.until(EC.visibility_of(tables_link))

            chairs_link = driver.find_element(By.XPATH, "//a[@href='/category/chairs']")
            wait.until(EC.visibility_of(chairs_link))

            # Checking for presence of the accept cookies button
            accept_cookies_btn = driver.find_element(By.ID, "rcc-confirm-button")
            wait.until(EC.visibility_of(accept_cookies_btn))

            # Checking for presence of the search input in subscribe section
            subscribe_input = driver.find_element(By.XPATH, "//input[@name='email']")
            wait.until(EC.visibility_of(subscribe_input))

            # Checking for presence of the Add to cart button on a product
            add_to_cart_btn = driver.find_element(By.XPATH, "//button[@title='Add to cart']")
            wait.until(EC.visibility_of(add_to_cart_btn))
        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")
        
        # 3. Interact with elements, click a button
        try:
            # Accept cookies
            accept_cookies_btn.click()

            # Clicking the add to cart button to verify UI interaction
            add_to_cart_btn.click()
            
            # Assuming there's a UI update or message after adding to cart
            cart_message = driver.find_element(By.XPATH, "//p[contains(text(), 'No items added to cart')]")
            wait.until(EC.visibility_of(cart_message))
        except Exception as e:
            self.fail(f"UI interaction failed: {e}")

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()