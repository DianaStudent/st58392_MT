from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_UI_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check visibility of footer
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

        # Check visibility of navigation
        nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
        self.assertTrue(nav.is_displayed(), "Navigation is not visible.")

        # Check presence of the elements in the main UI
        # Checking 'Contact us' link
        contact_us_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
        self.assertTrue(contact_us_link.is_displayed(), "Contact us link is not visible.")

        # Checking 'Sign in' link
        sign_in_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible.")

        # Checking 'Cart' icon
        cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "i.material-icons.shopping-cart")))
        self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible.")

        # Checking the presence and visibility of input fields and buttons in the search widget
        search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-widgets input[type='text']")))
        self.assertTrue(search_input.is_displayed(), "Search input field is not visible.")

        # Checking the main categories in the menu
        clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
        self.assertTrue(clothes_link.is_displayed(), "Clothes category link is not visible.")

        accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
        self.assertTrue(accessories_link.is_displayed(), "Accessories category link is not visible.")

        art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        self.assertTrue(art_link.is_displayed(), "Art category link is not visible.")

        # Interact with the element and confirm UI reaction
        art_link.click()
        current_url = driver.current_url
        self.assertEqual(current_url, "http://localhost:8080/en/9-art", "Art link did not navigate correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()