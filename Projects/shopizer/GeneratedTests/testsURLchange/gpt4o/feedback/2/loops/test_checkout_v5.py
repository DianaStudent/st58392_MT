from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        ).click()

        # Log in
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        ).click()

        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        ).send_keys("test22@user.com")

        driver.find_element(By.NAME, "loginPassword").send_keys("test**11")
        driver.find_element(By.XPATH, "//button[contains(., 'Login')]").click()

        # Navigate back to home
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Home"))
        ).click()

        # Hover over the first product
        product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-of-type(1) .product-img"))
        )
        ActionChains(driver).move_to_element(product).perform()

        # Click "Add to cart"
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']"))
        ).click()

        # Open cart popup
        driver.find_element(By.CLASS_NAME, "icon-cart").click()

        # Wait for popup and click "View cart"
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
        )
        driver.find_element(By.LINK_TEXT, "View Cart").click()

        # Click "Proceed to Checkout"
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
        ).click()

        # Fill out the billing form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "company"))
        ).send_keys("Comp1")

        driver.find_element(By.NAME, "address").send_keys("Street1")
        driver.find_element(By.NAME, "city").send_keys("Quebec")

        # Selecting Quebec from the dropdown
        select_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[contains(@class,'billing-select')]/option[text()='Quebec']"))
        )
        select_element.click()

        driver.find_element(By.NAME, "postalCode").send_keys("1234")
        driver.find_element(By.NAME, "phone").send_keys("1234567891")

        # Accept terms
        agree_checkbox = driver.find_element(By.NAME, "isAgree")
        if agree_checkbox:
            agree_checkbox.click()
        else:
            self.fail("Agree checkbox not found.")

        # Check if form is filled
        fields = driver.find_elements(By.NAME, "company")
        self.assertTrue(all(field.get_attribute('value') for field in fields), "Form not filled properly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()