from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestDemoPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements(self):
        wait = WebDriverWait(self.driver, 20)

        # Check the presence and visibility of the navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))
        except:
            self.fail("Navigation links are not properly displayed")

        # Check the presence and visibility of buttons and inputs
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "s")))
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
            wishlist_buttons = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".wishlist-button-add")))
        except:
            self.fail("Buttons or inputs are not properly displayed")

        # Interact with an element (click a wishlist button)
        try:
            wishlist_buttons[0].click()
            toast = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".wishlist-toast.isActive")))
        except:
            self.fail("Failed to interact with the wishlist button or UI update not observed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()