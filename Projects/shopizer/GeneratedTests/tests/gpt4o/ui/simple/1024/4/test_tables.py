import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header elements
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
        if not header.is_displayed():
            self.fail("Header is not visible.")

        # Check cookie consent button
        try:
            cookie_button = driver.find_element(By.ID, "rcc-confirm-button")
            wait.until(EC.visibility_of(cookie_button))
        except:
            self.fail("Cookie consent button is not visible.")

        # Check logo
        try:
            logo = driver.find_element(By.XPATH, "//a[@href='/']/img")
            wait.until(EC.visibility_of(logo))
        except:
            self.fail("Logo is not visible.")

        # Check navigation links
        nav_links = [
            ('Home', '/'),
            ('Tables', '/category/tables'),
            ('Chairs', '/category/chairs')
        ]

        for text, link in nav_links:
            try:
                nav_item = driver.find_element(By.XPATH, f"//a[text()='{text}']")
                wait.until(EC.visibility_of(nav_item))
                self.assertEqual(nav_item.get_attribute("href"), f"http://localhost{link}")
            except:
                self.fail(f"Navigation link '{text}' not visible or incorrect.")

        # Check Login and Register
        try:
            login_link = driver.find_element(By.XPATH, "//a[@href='/login']")
            wait.until(EC.visibility_of(login_link))

            register_link = driver.find_element(By.XPATH, "//a[@href='/register']")
            wait.until(EC.visibility_of(register_link))
        except:
            self.fail("Login/Register links are not visible.")

        # Check product elements
        try:
            product = driver.find_element(By.XPATH, "//div[@class='product-wrap']")
            wait.until(EC.visibility_of(product))
        except:
            self.fail("Products are not visible.")

        # Check footer elements
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        if not footer.is_displayed():
            self.fail("Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()