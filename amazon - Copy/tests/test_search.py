import time
import random
from login_test import AmazonLoginTest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonSearchTest():
    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None
        
    #initialie and perform AmazonLoginTest
    def logins(self):
        self.loggs= AmazonLoginTest(self.email, self.password, self.phone_number)
        self.loggs.login()
        self.driver = self.loggs.driver

    def test_search(self):
        driver = self.driver

        # Wait for the search bar to be visible
        print("Search query is going to be entered")
        search_bar = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH,'//*[@id="twotabsearchtextbox"]'))
        )
        time.sleep(10)

        # Search for a keyword
        search_bar.send_keys("fridge")
        search_bar.send_keys(Keys.RETURN)
        print("Search query is entered")
        time.sleep(10)

        # Wait for the search results to load
        print("\nSearch test case is executed\n")
        time.sleep(10)

        # Get a list of product elements
        products = driver.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]')

        # Select a random product
        random_product = random.choice(products)
        random_product.click()

        # Wait for 10 seconds
        time.sleep(10)

    def runtest(self):
        self.logins()
        self.test_search()

# Uncomment the below lines to test the search test case independently
# if __name__ == "__main__":
    # email = 'your email'
    # password = 'your password'
    # phone_number = 'your phone number'
#     search = AmazonSearchTest(email, password, phone_number)
#     search.runtest()