import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence_and_visibility(self):
        driver = self.driver

        # Wait for and check header
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "header"))
        )
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Wait for and check footer
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
        )
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check navigation links
        nav_links = [
            "/",
            "/newproducts",
            "/search",
            "/customer/info",
            "/blog",
            "/contactus"
        ]
        
        for link in nav_links:
            elem = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[@href='{link}']"))
            )
            self.assertTrue(elem.is_displayed(), f"Navigation link {link} is not visible")

        # Check the search input field
        search_box = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "small-searchterms"))
        )
        self.assertTrue(search_box.is_displayed(), "Search input field is not visible")

        # Check the search button
        search_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))
        )
        self.assertTrue(search_button.is_displayed(), "Search button is not visible")
        
        # Click on the search button and confirm the UI's behavior
        search_box.send_keys("test")
        search_button.click()
        WebDriverWait(driver, 20).until(
            EC.url_contains("/search?q=test"),
            f"Page did not navigate to search results as expected"
        )

        # Expecting the presence of notification bars in hidden state
        notification_bars = [
            "dialog-notifications-success",
            "dialog-notifications-error",
            "dialog-notifications-warning"
        ]

        for bar_id in notification_bars:
            notification_bar = driver.find_element(By.ID, bar_id)
            self.assertTrue(notification_bar.is_displayed() == False, f"Notification bar {bar_id} is unexpectedly visible")

    def test_interactions(self):
        driver = self.driver

        # Mouse over cart link to reveal flyout
        top_cart = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "topcartlink"))
        )
        ActionChains(driver).move_to_element(top_cart).perform()

        flyout_cart = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "flyout-cart"))
        )
        self.assertTrue(flyout_cart.is_displayed(), "Flyout cart is not visible upon interaction")

if __name__ == "__main__":
    unittest.main()