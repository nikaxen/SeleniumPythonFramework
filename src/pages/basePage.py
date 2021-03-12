import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class BasePage():
    """ Parent class for all page classes (contains generic methods) """

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    # Generic methods
    def el_get(self, locator, wait=20):
        try:
            return WebDriverWait(
                self.driver, wait).until(
                EC.visibility_of_element_located(locator))
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_click(self, locator):
        try:
            WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator)).click()
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_send_text(self, locator, text):
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_get_text(self, locator):
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return element.text
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_verify_title(self, expectedTitle):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(expectedTitle))
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_is_visible(self, locator):
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            return True
        except BaseException:
            return False

    def el_is_clickable(self, locator):
        try:
            return WebDriverWait(
                self.driver, 10).until(
                EC.element_to_be_clickable(locator))
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_is_presented(self, locator):
        try:
            return WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(locator))
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_hover(self, locator):
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            ActionChains(self.driver).move_to_element(element).perform()
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_get_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
            return self.driver.title
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def el_get_title_part(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains(title))
            return self.driver.title
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def select_el_option(self, locator, menuItem):
        try:
            element = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            for option in element.find_elements_by_tag_name('option'):
                if option.text == menuItem:
                    option.click()
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def selectItemFromList(self, DDMenuBtn, DDUL, menuItem):
        try:
            # Find DropDown button and click
            WebDriverWait(
                self.driver, 20).until(
                EC.visibility_of_element_located(DDMenuBtn)).click()
            # Find ul of menu items
            dd_ul = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(DDUL))
            # Put all li elements into list
            menuItems = dd_ul.find_elements_by_tag_name("li")
            # Loop through li elements and find desired menuItem
            for item in menuItems:
                text = item.text.lower()
                if text == menuItem.lower():
                    item.click()
                    print("item selected: " + text)
                    break
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)

    def verifyElementTextIs(self, locator, expectedText):
        try:
            el = WebDriverWait(
                self.driver, 10).until(
                EC.visibility_of_element_located(locator))
            if el.text == expectedText:
                return True
            else:
                return False
        except BaseException:
            e = sys.exc_info()[0]
            print("!!! Exception: ", e)
