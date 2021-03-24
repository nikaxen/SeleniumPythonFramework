from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class Config():

    BASE_URL = "https://www.google.com"

    def getDriver(self, driver_name):
        if driver_name == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        elif driver_name == "firefox":
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif driver_name == "safari":
            driver = webdriver.Safari()
        else:
            raise Exception("driver '{}' not found".format(driver_name))
        driver.implicitly_wait(5)
        return driver