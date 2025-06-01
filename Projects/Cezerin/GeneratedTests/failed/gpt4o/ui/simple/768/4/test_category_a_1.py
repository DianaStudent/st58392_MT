from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Header elements
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//header//a[@class='logo-image']"))
            )
        except:
            self.fail("Logo is not visible")
        
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//input[@class='search-input']"))
            )
        except:
            self.fail("Search input is not visible")

        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='icon icon-search']"))
            )
        except:
            self.fail("Search icon is not visible")

        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//span[@class='cart-button']"))
            )
        except:
            self.fail("Cart button is not visible")
        
        # Navigation links
        for category in ["Category A", "Category B", "Category C"]:
            try:
                self.wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH, f"//a[text()='{category}']"
                    ))
                )
            except:
                self.fail(f"{category} link is not visible")

        # Breadcrumbs
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//nav[@class='breadcrumb']//a"))
            )
        except:
            self.fail("Breadcrumbs are not visible")

        # Sort dropdown
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//select"))
            )
        except:
            self.fail("Sort dropdown is not visible")
        
        # Footer elements
        try:
            self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//footer//div[@class='footer-logo']"))
            )
        except:
            self.fail("Footer logo is not visible")
        
        for footer_link in ["About", "Blog", "Terms of Service", "Privacy Policy"]:
            try:
                self.wait.until(
                    EC.visibility_of_element_located((
                        By.XPATH, f"//a[text()='{footer_link}']"
                    ))
                )
            except:
                self.fail(f"Footer link {footer_link} is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()