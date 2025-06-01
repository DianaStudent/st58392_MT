import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='logo']/a/img")))
            self.assertTrue(logo.is_displayed(), "Logo not displayed")
        except:
            self.fail("Logo is missing")

        # Check navigation links
        for nav_link in ["Home", "Tables", "Chairs"]:
            try:
                nav = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, nav_link)))
                self.assertTrue(nav.is_displayed(), f"{nav_link} link not displayed")
            except:
                self.fail(f"{nav_link} link is missing")

        # Check cookie consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed(), "Cookie consent button not displayed")
        except:
            self.fail("Cookie consent button is missing")

        # Click "Accept" cookie button
        try:
            cookie_button.click()
        except:
            self.fail("Cannot click cookie consent button")

        # Verify interactive button
        try:
            shop_now_button = wait.until(EC.visibility_of_element_located
                                         ((By.XPATH, "//a[@class='btn btn-black rounded-0']")))
            self.assertTrue(shop_now_button.is_displayed(), "Shop Now button not displayed")
            shop_now_button.click()
        except:
            self.fail("Shop Now button is missing or clickable")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()