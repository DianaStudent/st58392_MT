import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
            accessories_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
            art_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")
        except Exception as e:
            self.fail(f"Navigation links are not visible: {e}")

        # Verify presence of login and registration links
        try:
            login_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")
            register_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/registration']")
        except Exception as e:
            self.fail(f"Login or Register link is not visible: {e}")

        # Verify search input is visible
        try:
            search_input = driver.find_element(By.XPATH, "//input[@placeholder='Search our catalog']")
        except Exception as e:
            self.fail(f"Search input is not visible: {e}")

        # Verify presence of a product and interact with its wishlist button
        try:
            product_thumbnail = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='Hummingbird printed t-shirt']")))
            wishlist_button = driver.find_element(By.CSS_SELECTOR, "button.wishlist-button-add")
            wishlist_button.click()
        except Exception as e:
            self.fail(f"Product thumbnail or wishlist button is not interactive: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()