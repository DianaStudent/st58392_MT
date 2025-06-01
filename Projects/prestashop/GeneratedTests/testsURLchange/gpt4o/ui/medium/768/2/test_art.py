import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestArtPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/9-art")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check main header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertTrue(header.is_displayed(), "Header not displayed")

        # Check banner
        header_banner = driver.find_element(By.CLASS_NAME, "header-banner")
        self.assertTrue(header_banner.is_displayed(), "Header banner not displayed")

        # Check navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
        self.assertTrue(home_link.is_displayed(), "Home link not displayed")

        clothes_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
        self.assertTrue(clothes_link.is_displayed(), "Clothes link not displayed")

        accessories_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
        self.assertTrue(accessories_link.is_displayed(), "Accessories link not displayed")

        art_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))
        self.assertTrue(art_link.is_displayed(), "Art link not displayed")

        # Check login link
        login_link = driver.find_element(By.LINK_TEXT, "Sign in")
        self.assertTrue(login_link.is_displayed(), "Sign in link not displayed")

        # Check register link
        register_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")
        self.assertTrue(register_link.is_displayed(), "Register link not displayed")

        # Interact with the first product's quick view button
        quick_view_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='quick-view js-quick-view']")))
        quick_view_button.click()

        # Check if the quick view modal appears
        quick_view_modal = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-modal")))
        self.assertTrue(quick_view_modal.is_displayed(), "Quick view modal not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()