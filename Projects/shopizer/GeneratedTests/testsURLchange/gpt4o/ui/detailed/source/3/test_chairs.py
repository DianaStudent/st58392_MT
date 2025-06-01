import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Setup Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver

        # Wait for header to be visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header[@class='header-area clearfix']"))
        )

        # Check presence and visibility of navigation links
        home_link = driver.find_element(By.XPATH, "//a[text()='Home']")
        tables_link = driver.find_element(By.XPATH, "//a[text()='Tables']")
        chairs_link = driver.find_element(By.XPATH, "//a[text()='Chairs']")
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Check for 'Accept' cookies button
        accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")

        # Click 'Accept' cookies button
        accept_cookies_button.click()

        # Check presence and visibility of footer
        footer = driver.find_element(By.XPATH, "//footer[@class='footer-area bg-gray pt-100 pb-70']")
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check for 'Login' and 'Register' links
        login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
        register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Check for product listing section
        product_section = driver.find_element(By.XPATH, "//div[@class='shop-area pt-95 pb-100']")
        self.assertTrue(product_section.is_displayed(), "Product section is not visible")

    def tearDown(self):
        # Close the driver
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()