from selenium import webdriver
from pages.basePage import BasePage
from locators.sampleLocators import SampleLocators

class SamplePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)