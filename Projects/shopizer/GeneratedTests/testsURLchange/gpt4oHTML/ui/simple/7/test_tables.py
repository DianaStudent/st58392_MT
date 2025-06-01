import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        try:
            # Check header components
            header_area = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            self.assertTrue(header_area.is_displayed())
            
            # Check links in the main menu
            main_menu = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
            self.assertTrue(main_menu.is_displayed())
            
            links = main_menu.find_elements(By.TAG_NAME, "a")
            expected_links = [
                ("Home", "/"),
                ("Tables", "/category/tables"),
                ("Chairs", "/category/chairs")
            ]

            for link_text, href in expected_links:
                link = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, f"//a[text()='{link_text}' and @href='{href}']"))
                )
                self.assertTrue(link.is_displayed())

            # Check 'Accept Cookies' button
            cookie_button = self.wait.until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
            self.assertTrue(cookie_button.is_displayed())

            # Check 'Login' and 'Register' links
            account_dropdown = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-dropdown")))
            self.assertTrue(account_dropdown.is_displayed())

            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
            )
            self.assertTrue(login_link.is_displayed())

            register_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/register']"))
            )
            self.assertTrue(register_link.is_displayed())

            # Check Cart icon
            cart_icon = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            self.assertTrue(cart_icon.is_displayed())

            # Check product sections
            product_wraps = self.wait.until(
                EC.visibility_of_all_elements_located((By.CLASS_NAME, "product-wrap"))
            )
            self.assertGreaterEqual(len(product_wraps), 4)

        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

if __name__ == "__main__":
    unittest.main()