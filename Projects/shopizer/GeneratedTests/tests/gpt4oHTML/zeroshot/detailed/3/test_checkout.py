import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080")  # URL is assumed

    def test_checkout_process(self):
        driver = self.driver
        
        # 1. Open the home page
        self.wait.until(EC.presence_of_element_located((By.ID, "root")))
        
        # 2. Log in using credentials
        driver.find_element(By.CLASS_NAME, 'account-setting-active').click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login'))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, 'username'))).send_keys("test22@user.com")
        driver.find_element(By.NAME, 'loginPassword').send_keys("test**11")
        login_button = driver.find_element(By.XPATH, "//button[span='Login']")
        self.wait.until(EC.element_to_be_clickable(login_button)).click()
        
        # Use WebDriverWait to ensure the user is logged in, check for a greeting message which indicates login success
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-name")))

        # 3. Navigate back to the home page
        driver.find_element(By.XPATH, "//a[text()='Home']").click()

        # 4. Hover over the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:first-of-type .product-img")))
        ActionChains(driver).move_to_element(first_product).perform()

        # 5. Click the revealed "Add to cart" button
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-wrap-2:first-of-type .fa-shopping-cart"))).click()

        # 6. Click the cart icon to open the popup cart
        driver.find_element(By.CLASS_NAME, 'icon-cart').click()

        # 7. Wait for the popup to become visible
        cart_popup = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # 8. Click "View cart" or similar button inside the popup
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
        self.wait.until(EC.element_to_be_clickable(view_cart_button)).click()

        # 9. On the cart page, click the "Proceed to Checkout" button
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))).click()

        # 10. Fill out the billing form
        self.wait.until(EC.presence_of_element_located((By.NAME, 'company'))).send_keys("Comp1")
        driver.find_element(By.NAME, 'address').send_keys("Street1")
        driver.find_element(By.NAME, 'city').send_keys("Quebec")

        # Use the label to select "Quebec" within a dropdown for the region
        region_dropdown = driver.find_element(By.XPATH, "//label[text()='State']/following-sibling::select")
        region_dropdown.click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//option[text()='Quebec']"))).click()

        driver.find_element(By.NAME, 'postalCode').send_keys("1234")
        driver.find_element(By.NAME, 'phone').send_keys("1234567891")
        accept_terms = driver.find_element(By.XPATH, "//label[contains(., 'I agree with the terms and conditions')]/preceding-sibling::input")
        if not accept_terms.is_selected():
            accept_terms.click()

        # 11. Wait for any maps popups or warnings and close them
        # Not applicable here as no popups are described, but included for completeness
        try:
          self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "some-map-popup-class"))).click()
        except:
          pass  # Continue if not present

        # Verify form is filled (using one of the input values as a measure of success)
        assert_field = driver.find_element(By.NAME, 'company').get_attribute('value')
        if assert_field != "Comp1":
            self.fail("Form not filled successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()