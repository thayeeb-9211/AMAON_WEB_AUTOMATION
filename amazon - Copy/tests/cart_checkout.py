import time
import random
from test_search import AmazonSearchTest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class AmazonCartTest():
    def __init__(self, email, password, phone_number):
        super().__init__()
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.driver = None
        
    #initialie and perform AmazonLoginTest
    def searches(self):
        self.searching= AmazonSearchTest(self.email, self.password, self.phone_number)
        self.searching.runtest()
        self.driver = self.searching.driver

    def test_cart(self):
        driver = self.driver

    # Scroll down to the "Add to Cart" button
        driver.execute_script("window.scrollBy(0, 600);")
        time.sleep(10)

        try:

            product_elements = driver.find_elements(By.XPATH, '//span[contains(@class, "a-size-medium a-color-base a-text-normal")]')
            product_names = [product.text for product in product_elements]

            # Print the product names
            print("Product Names:")
            for product_name in product_names:
                print(product_name)

            # Select a random product name
            random_product = random.choice(product_names)
            print(f"\nSelected Random Product: {random_product}")

            # Find the corresponding product element again
            random_product_element = next(
                (product for product in product_elements if product.text == random_product), None
            )

            if random_product_element:
                # Retrieve the product ID (you may need to adjust this based on the actual page structure)
                product_id = random_product_element.get_attribute('data-asin')
                print(f"Product ID: {product_id}")
            time.sleep(10)
            print('Clicked "Add to Cart" button')
        except NoSuchElementException as e:
            print(f'Error clicking "Add to Cart" button: {e}')
            return

        # Wait for the "Proceed to Checkout" button to appear
        try:
            goto_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="sw-gtc"]'))
            )
            goto_button.click()

            time.sleep(10)
            print('Clicked "Go to Cart" button')
        except NoSuchElementException as e:
            print(f'Error clicking "Proceed to Checkout" button: {e}')

        # Wait for the "Proceed to Checkout" button to appear
        try:
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*/span/input[@aria-labelledby="sc-buy-box-ptc-button-announce" and @name="proceedToRetailCheckout"]'))
            )
            checkout_button.click()

            time.sleep(10)
            print('Clicked "Proceed to Checkout" button')
        except NoSuchElementException as e:
            print(f'Error clicking "Proceed to Checkout" button: {e}')


    def runtest(self):
        self.searches()
        self.test_cart()

# Uncomment the below lines to test the cart_checkout code test independently
if __name__ == "__main__":
    email = 'your email'
    password = 'your password'
    phone_number = 'your phone number'
    cart = AmazonCartTest(email, password, phone_number)
    cart.runtest()