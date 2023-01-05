import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

class Whatsapp:

    def do_action(self, phone_number:str, message:str, times: int):
        #phone_number ="+9613721112"
        #message = "Magic of PYTHON ;)"

        chrome_options = Options()
        chrome_options.add_experimental_option("detach",True)

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://web.whatsapp.com/send?phone="+phone_number)

        self._checkAllLoaded(driver)

        for x in range(times):
            search_input = driver.find_element(By.XPATH,
                                               "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]")
            search_input.send_keys(message)
            search_input.send_keys(Keys.ENTER)
            time.sleep(0.5)

        print("All Done!")

    def _checkAllLoaded(self, driver):
        while self._checkQrCodeScanned(driver):
            print("Waiting for code to be scanned!")
            time.sleep(5)

        print("Code Scanned!!")

        while self._checkSearchLoaded(driver):
            print("Waiting for search to load")
            time.sleep(5)

        print("Search Loaded!!")


    def _checkQrCodeScanned(self, driver):
        try:
            qr_code= driver.find_element(By.XPATH, "//*[@id=\"app\"]/div/div/div[3]/div[1]/div/div[2]/div")
        except NoSuchElementException:
            return False
        return True

    def _checkSearchLoaded(self, driver):
        try:
            search_input= driver.find_element(By.XPATH, "//*[@id=\"main\"]/footer/div[1]/div/span[2]/div/div[2]/div[1]")
        except NoSuchElementException:
            return True
        return False
