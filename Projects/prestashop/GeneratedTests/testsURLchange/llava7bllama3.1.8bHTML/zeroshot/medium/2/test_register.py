import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegister(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_register(self):
        # 1. Open the home page.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#top-menu")))

        # 2. Click on the login link in the top menu.
        self.driver.find_element(By.LINK_TEXT, "Login").click()

        # 3. Click on the register link on the login page.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Register"))).click()

        # 4. Fill in the registration form fields:
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "gender"))).send_keys("Male")
        self.driver.find_element(By.NAME, "first_name").send_keys("John")
        self.driver.find_element(By.NAME, "last_name").send_keys("Doe")
        email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        email.send_keys(f"test_{self.random_string()}@user.com")
        self.driver.find_element(By.ID, "password").send_keys("test@user1")
        birthdate = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "birthdate")))
        birthdate.send_keys("1990-01-01")

        # 5. Check required checkboxes.
        self.driver.find_element(By.NAME, "terms").click()
        self.driver.find_element(By.NAME, "cookies").click()

        # 6. Submit the form.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#register-button"))).click()

        # 7. Confirm success by checking for the presence of "Sign out" in the top bar.
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertIn("Sign out", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

    def random_string(self):
        import random
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(5))

if __name__ == "__main__":
    unittest.main()