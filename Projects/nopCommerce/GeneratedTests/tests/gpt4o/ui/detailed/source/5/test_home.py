import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header is visible
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify footer is visible
        footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Verify input fields and buttons
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible")

        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
        self.assertTrue(search_button.is_displayed(), "Search button is not visible")

        newsletter_input = self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-email')))
        self.assertTrue(newsletter_input.is_displayed(), "Newsletter input is not visible")

        newsletter_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'newsletter-subscribe-button')))
        self.assertTrue(newsletter_button.is_displayed(), "Newsletter button is not visible")

        # Verify navigation links
        nav_links = ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']
        for link_text in nav_links:
            link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"Navigation link '{link_text}' is not visible")

        # Interact with UI elements
        cart_link = self.wait.until(EC.visibility_of_element_located((By.ID, 'topcartlink')))
        cart_link.click()

        flyout_cart = self.wait.until(EC.visibility_of_element_located((By.ID, 'flyout-cart')))
        self.assertTrue(flyout_cart.is_displayed(), "Flyout cart is not visible after clicking cart link")

        # Check for notifications bar
        notifications_bar = self.wait.until(EC.visibility_of_element_located((By.ID, 'bar-notification')))
        self.assertTrue(notifications_bar.is_displayed(), "Notification bar is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()