import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        # Check headers and links
        try:
            # Header links
            headers = [
                "/register?returnUrl=%2F",
                "/login?returnUrl=%2F",
                "/wishlist",
                "/cart",
                "/"
            ]
            for header in headers:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{header}']")))
                self.assertTrue(element.is_displayed())

            # Main navigation links
            nav_links = [
                "/",
                "/newproducts",
                "/search",
                "/customer/info",
                "/blog",
                "/contactus"
            ]
            for link in nav_links:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//ul[@class='top-menu notmobile']//a[@href='{link}']")))
                self.assertTrue(element.is_displayed())

            # Search form
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
            self.assertTrue(search_input.is_displayed())
            self.assertTrue(search_button.is_displayed())

            # Footer links
            footer_links = [
                "/sitemap",
                "/shipping-returns",
                "/privacy-notice",
                "/conditions-of-use",
                "/about-us",
                "/contactus",
                "/search",
                "/news",
                "/recentlyviewedproducts",
                "/compareproducts",
                "/newproducts",
                "/customer/info",
                "/order/history",
                "/customer/addresses",
                "/vendor/apply"
            ]
            for link in footer_links:
                element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@class='footer']//a[@href='{link}']")))
                self.assertTrue(element.is_displayed())

            # Newsletter components
            newsletter_email = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-email")))
            newsletter_button = wait.until(EC.visibility_of_element_located((By.ID, "newsletter-subscribe-button")))
            self.assertTrue(newsletter_email.is_displayed())
            self.assertTrue(newsletter_button.is_displayed())

        except Exception as e:
            self.fail(f"Element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()