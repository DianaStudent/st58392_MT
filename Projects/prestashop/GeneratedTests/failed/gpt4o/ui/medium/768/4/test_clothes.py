from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class ClothesPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait
        
        try:
            # Check for header
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check for navigation links
            nav = driver.find_element(By.CLASS_NAME, "header-nav")
            contact_us_link = nav.find_element(By.LINK_TEXT, "Contact us")
            language_selector = nav.find_element(By.ID, "_desktop_language_selector")
            sign_in_link = nav.find_element(By.LINK_TEXT, "Sign in")
            cart_icon = nav.find_element(By.CLASS_NAME, "shopping-cart")

            # Check for main UI components
            main = driver.find_element(By.ID, "main")
            category_title = main.find_element(By.TAG_NAME, "h1")
            subcategories = main.find_element(By.CLASS_NAME, "subcategories-list")
            products_section = main.find_element(By.ID, "products")

            # Check for footer
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            newsletter_input = footer.find_element(By.NAME, "email")

            # Assertions for visibility
            self.assertTrue(header.is_displayed(), "Header is not visible")
            self.assertTrue(contact_us_link.is_displayed(), "Contact us link is not visible")
            self.assertTrue(language_selector.is_displayed(), "Language selector is not visible")
            self.assertTrue(sign_in_link.is_displayed(), "Sign in link is not visible")
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")
            self.assertTrue(category_title.is_displayed(), "Category title is not visible")
            self.assertTrue(subcategories.is_displayed(), "Subcategories are not visible")
            self.assertTrue(products_section.is_displayed(), "Products section is not visible")
            self.assertTrue(newsletter_input.is_displayed(), "Newsletter input is not visible")

            # Interaction: Click "Sign in" link
            sign_in_link.click()
            sign_in_url = "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes"
            wait.until(EC.url_to_be(sign_in_url))
            self.assertEqual(driver.current_url, sign_in_url, "Sign in URL did not load correctly")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()