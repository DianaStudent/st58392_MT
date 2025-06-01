import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestWebsite(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_visibility(self):
        try:
            # Verify header and main navigation
            header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            self.assertIsNotNone(header, "Header is missing.")

            # Verify menu links
            menu_links = ["Home", "Tables", "Chairs"]
            for link_text in menu_links:
                element = self.wait.until(
                    EC.visibility_of_element_located((By.LINK_TEXT, link_text))
                )
                self.assertIsNotNone(element, f"Menu link '{link_text}' is missing.")

            # Verify login and register links
            login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            self.assertIsNotNone(login_link, "Login link is missing.")
            
            register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
            self.assertIsNotNone(register_link, "Register link is missing.")

            # Verify product section and action buttons
            product_section = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'product-area'))
            )
            self.assertIsNotNone(product_section, "Product section is missing.")

            action_buttons = product_section.find_elements(By.TAG_NAME, 'button')
            self.assertGreater(len(action_buttons), 0, "Action buttons are missing in product section.")

            # Verify subscription form
            subscribe_form = self.wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, 'form'))
            )
            self.assertIsNotNone(subscribe_form, "Subscription form is missing.")
            
            email_input = subscribe_form.find_element(By.NAME, 'email')
            self.assertIsNotNone(email_input, "Email input in subscription form is missing.")
            self.assertTrue(email_input.is_displayed(), "Email input is not visible.")

            subscribe_button = subscribe_form.find_element(By.TAG_NAME, 'button')
            self.assertIsNotNone(subscribe_button, "Subscribe button is missing.")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible.")

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")


if __name__ == "__main__":
    unittest.main()