import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check header elements
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.header")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-login")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-wishlist")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-cart")))

        # Check search box
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#small-searchterms")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))

        # Check navigation menu
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile")))

        menu_links = [
            "/",
            "/newproducts",
            "/search",
            "/customer/info",
            "/blog",
            "/contactus"
        ]

        for link in menu_links:
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, f"a[href='{link}']").is_displayed())

        # Check footer elements
        footer_titles = [
            "Information",
            "Customer service",
            "My account",
            "Follow us"
        ]

        for title in footer_titles:
            self.assertTrue(driver.find_element(By.XPATH, f"//div[@class='title']/strong[text()='{title}']").is_displayed())

        # Check newsletter subscription
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#newsletter-email")))
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button#newsletter-subscribe-button")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()