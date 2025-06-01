from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")
        
        try:
            # Verify header
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Verify footer
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))

            # Verify navigation
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))

            # Verify search widget
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "search_widget")))

            # Verify sign in
            sign_in = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Sign in")))
            self.assertTrue(sign_in.is_displayed(), "Sign in button is not visible")

            # Verify cart
            cart = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))
            self.assertTrue(cart.is_displayed(), "Cart is not visible")

            # Verify product section
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "featured-products")))

            # Click on 'Clothes' category
            clothes_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Clothes")))
            clothes_link.click()
            WebDriverWait(driver, 20).until(EC.url_to_be("http://localhost:8080/en/3-clothes"))

            # Return to home
            home_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
            home_link.click()
            WebDriverWait(driver, 20).until(EC.url_to_be("http://localhost:8080/en/"))

        except Exception as e:
            self.fail(f"Test failed due to missing UI element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()