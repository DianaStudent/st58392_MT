import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Check the presence of main navigation links
        home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
        clothes_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
        accessories_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")))
        art_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

        # Check the presence of login and register links
        login_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        register_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))

        # Check the presence of search input
        search_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s'][@placeholder='Search our catalog']")))

        # Check the presence of the cart icon
        cart_icon = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart")))

        # Interact with the wishlist button
        wishlist_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "wishlist-button-add")))
        wishlist_button.click()

        # Check for any errors after interaction (can be adapted to check specific UI changes)
        # Here we're assuming no exceptions are thrown
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()