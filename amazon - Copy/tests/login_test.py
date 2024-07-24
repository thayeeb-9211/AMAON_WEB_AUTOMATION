import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AmazonLoginTest():
    def __init__(self, email, password, phone_number):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def login(self):
        driver = self.driver
        amazon = 'https://www.amazon.in/'

        try:
            driver.get(amazon)
            print("Got in amazon's den..!!")
            time.sleep(10)
             
            print("Goiing to click on SIgn in Button...")
            sign_in_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]'))
            )
            sign_in_button.click()
            print("Clicked Sign in.")
            time.sleep(15)

            print("Going to Enter the email")
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="ap_email"]'))
            )
            email_input.send_keys(self.email)
            print("Email Entered")
            time.sleep(15)

            print("Continue Button is going to be clicked.")
            continue_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="continue"]'))
            )
            continue_button.click()
            print("Next Button CLicked.")
            time.sleep(10)

            print("Going to Enter the password")
            password_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="ap_password"]'))
            )
            password_input.send_keys(self.password)
            print("Password Entered")
            time.sleep(10)

            print("Going to click on keep me signed in button.")
            keep_button = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[2]/div/form/div/div[2]/div/div/label/div/label/input'))
            )
            keep_button.click()
            print("Button is CLicked")
            time.sleep(10)

            print("Next Button going to be clicked.")
            next_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="auth-signin-button"]'))
            )
            next_button.click()
            print("Next Button CLicked.")
            time.sleep(10)

            print("\nLogin-test is successfully completed.\n")

            return driver
        except Exception as e:
            print(f"Error: {e}")
            print("Unable to open Amazon")

# Uncomment the below lines to test the login code test independently
# if __name__ == "__main__":
    # email = 'your email'
    # password = 'your password'
    # phone_number = 'your phone number'
#     login = AmazonLoginTest(email, password, phone_number)
#     login.login()















            # if driver.current_url != amazon:
            #     try:
            #         print("Checking whthere Recovery phone Page appeared or not.")
                    
            #         try:
            #             print("Finding the Confirm PHone div")
            #             element = WebDriverWait(driver, 20).until(
            #                 EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Confirm your recovery phone number')]"))
            #             )
                       
                        
            #             element.click()
            #             print("Found the Confirm PHone div")
            #         except :
            #             print("Unable to find  the Confirm PHone div")
            #         try:
            #             print("Trying to click Dropdown menu")
            #             dropdown_menu = WebDriverWait(driver, 20).until(
            #                 EC.element_to_be_clickable((By.XPATH, "//*[@id='countryList']/div/div[1]/div[2]"))
            #             )
            #             dropdown_menu.click()
            #             print("clicked Dropdown menu")
            #         except :
            #             print("Unable to click Dropdown menu")

            #         try:
            #             print("Trying to Select India from the list")
            #             india_option = WebDriverWait(driver, 10).until(
            #                 EC.element_to_be_clickable((By.XPATH, "//li[@data-value='in']"))
            #             )
      
            #             india_option.click()
            #             print("India got successfully")
            #         except :
            #             print("India did'nt got")

            #         try:
            #             print("Trying to input number")
            #             phone_input = WebDriverWait(driver, 10).until(
            #                 EC.visibility_of_element_located((By.XPATH, "//input[@type='tel']"))
            #             )
            #             phone_input.send_keys(self.phone_number)
            #             print("Number input successfully")
            #         except :

            #             print("Unable to input Number")

            #         try :
            #             print("Finding Next button")
            #             # Wait until the "Next" button is present in the DOM and visible
            #             next_button = WebDriverWait(driver, 20).until(
            #                 EC.visibility_of_element_located((By.XPATH, "//*[text()='Next']"))
            #             )

            #             # Wait until the "Next" button is clickable
            #             next_button = WebDriverWait(driver, 20).until(
            #                 EC.element_to_be_clickable((By.XPATH, "//*[text()='Next']"))
            #             )
            #             next_button.click()
            #             print("Next button clicked successfuly")
            #         except:
            #             print("Nexxt button not found or clicked.")
            #         time.sleep(20)
            #     except Exception as e:
            #         print(f"Error: {e}")
            #         print("Recovery phone Page not appeared")

            #     try:
            #         not_now_button = WebDriverWait(driver, 10).until(
            #             EC.element_to_be_clickable((By.XPATH, "//button[text()='Not now']"))
            #         )
            #         not_now_button.click()
            #         time.sleep(20)
            #     except Exception as e:
            #         print(f"Error: {e}")
            #         print("Passkey Page not appeared")