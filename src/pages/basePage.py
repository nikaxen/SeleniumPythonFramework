from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    """ Parent class for all page classes (contains generic methods) """

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Generic methods
    def el_get(self, locator, wait=20):
        return WebDriverWait(self.driver, wait).until(EC.visibility_of_element_located(locator))

    def el_click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def el_send_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def el_get_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def el_verify_title(self, expectedTitle):
        WebDriverWait(self.driver, 10).until(EC.title_is(expectedTitle))

    def el_is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
            return True
        except:
            return False

    def el_get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def select_el_option(self, by_locator, menuItem):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        for option in element.find_elements_by_tag_name('option'):
            if option.text == menuItem:
                option.click()

    def selectItemFromList(self, DDMenuBtn, DDUL, menuItem):
        #find DropDown button and click
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(DDMenuBtn)).click()
        #find ul of menu items
        dd_ul = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DDUL))
        #put all li elements into list
        menuItems = dd_ul.find_elements_by_tag_name("li")
        #loop through li elements and find desired menuItem
        for item in menuItems:
            text = item.text.lower()
            if text == menuItem.lower():
                item.click()
                print("item selected: " + text)
                break

    def verifyElementTextIs(self, loc, expectedText):
        el = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
        if el.text == expectedText:
            return True
        else:
            return False