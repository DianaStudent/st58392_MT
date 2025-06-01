from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver

        # Wait up to 20 seconds for element visibility
        wait = WebDriverWait(driver, 20)

        # Check header is present and visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        except:
            self.fail("Header not found or not visible")

        # Check navigation links
        for link_text in ["Home", "Tables", "Chairs"]:
            try:
                link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            except:
                self.fail(f"{link_text} link not found or not visible")

        # Check footer is present and visible
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area")))
        except:
            self.fail("Footer not found or not visible")

        # Check cookie consent button is present and visible
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        except:
            self.fail("Cookie Consent Button not found or not visible")

        # Check and interact with account buttons
        try:
            account_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Account setting button or Login/Register links not found or not visible")

        # Check product and add to cart button
        try:
            product_img = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.default-img")))
            add_to_cart_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]")))
        except:
            self.fail("Product image or Add to cart button not found or not visible")

        # Interact with add to cart button
        try:
            add_to_cart_button.click()
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        except:
            self.fail("Add to cart button not responsive or cart icon not visible")

        print("All UI elements are present and interactable.")

if __name__ == "__main__":
    unittest.main()