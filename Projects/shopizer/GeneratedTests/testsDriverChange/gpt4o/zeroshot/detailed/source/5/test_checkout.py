from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCheckoutProcess(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the home page
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logo img")))
        
        # Step 2: Log in using credentials
        driver.find_element(By.CSS_SELECTOR, ".account-setting-active").click()
        driver.find_element(By.LINK_TEXT, "Login").click()
        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys("test22@user.com")
        driver.find_element(By.NAME, "loginPassword").send_keys("test**11")
        driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']").click()
        
        # Step 3: Navigate back to the home page
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-name")))
        driver.find_element(By.CSS_SELECTOR, ".logo a").click()
        
        # Step 4: Hover over the first product and add to cart
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        product.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").click()
        
        # Step 5: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()
        
        # Step 6: Wait for the popup to become visible
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        
        # Step 7: Click "View cart" or similar button inside the popup
        driver.find_element(By.LINK_TEXT, "View Cart").click()
        
        # Step 8: On the cart page, click the "Proceed to Checkout" button
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))).click()
        
        # Step 9: Fill out the billing form
        wait.until(EC.presence_of_element_located((By.NAME, "company"))).send_keys("Comp1")
        driver.find_element(By.NAME, "address").send_keys("Street1")
        driver.find_element(By.NAME, "city").send_keys("Quebec")
        state_select = driver.find_element(By.CSS_SELECTOR, ".billing-select select")
        state_select.find_element(By.XPATH, "//option[text()='Quebec']").click()
        driver.find_element(By.NAME, "postalCode").send_keys("1234")
        driver.find_element(By.NAME, "phone").send_keys("1234567891")
        
        # Accept terms
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()
        
        # Confirm form is filled
        filled = all([
            driver.find_element(By.NAME, "company").get_attribute("value") == "Comp1",
            driver.find_element(By.NAME, "address").get_attribute("value") == "Street1",
            driver.find_element(By.NAME, "city").get_attribute("value") == "Quebec",
            state_select.get_attribute("value") == "QC",
            driver.find_element(By.NAME, "postalCode").get_attribute("value") == "1234",
            driver.find_element(By.NAME, "phone").get_attribute("value") == "1234567891",
            terms_checkbox.is_selected(),
        ])
        
        if not filled:
            self.fail("Not all fields are filled correctly!")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()