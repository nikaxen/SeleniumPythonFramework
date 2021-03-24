import unittest
import pytest
from selenium import webdriver
from config.config import Config
from locators.teacherAssistantLocators import TeacherAssistantLocators
from pages.teacherAssistantPage import teacherAssistantPage


class TeacherAssistanceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Config.getDriver(cls, "chrome")
        cls.driver.delete_all_cookies()
        cls.driver.maximize_window()
        cls.URL = Config.BASE_URL
        cls.tap = teacherAssistantPage(cls.driver)

    def getStaticPage(self):
        self.URL += "/pages/teacher-assistant/"
        self.driver.get(self.URL)

    def testTC1(self):
        """
        Verify 'Introducing Teacher Assistant' notification presents on a page
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_INTRODUCING_TEACHER_ASSISTANCE,
            'Introducing Teacher Assistant') == True

    def testTC2(self):
        """
        Verify 'A FREE Assistant for Every Teacher' text presents on a page
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_A_FREE_ASSISTANT_FOR_EVERY_TEACHER,
            'A FREE Assistant for Every Teacher') == True

    def testTC3(self):
        """
        Verify 'Save time and improve student outcomes with a platform that empowers how you teach.' text presents on a page
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_SAVE_TIME_AND_IMPROVE,
            'Save time and improve student outcomes with a platform that empowers how you teach.') == True

    def testTC4(self):
        """
        Verify 'Take a tour' button presents on a page
        """
        self.getStaticPage()
        assert self.tap.el_is_visible(
            TeacherAssistantLocators.BUTTON_TAKE_A_TOUR) == True

    def testTC5(self):
        """
        Verify 'Choose your subject' link presents on a page
        """
        self.getStaticPage()
        assert self.tap.el_is_visible(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT) == True

    def testTC6(self):
        """
        Verify 'Choose your subject' link opens a popup when clicked on it
        """
        self.getStaticPage()
        assert self.tap.tc6() == True

    def testTC7(self):
        """
        Verify 'Choose your subject' popup has a close link and it closes the popup
        """
        self.getStaticPage()
        assert self.tap.tc7() == True

    def testTC8(self):
        """
        Verify 'Choose your subject' popup has a title
        """
        self.getStaticPage()
        assert self.tap.tc8() == True

    def testTC9(self):
        """
        Verify 'Choose your subject' popup has a description
        """
        self.getStaticPage()
        assert self.tap.tc9() == True

    def testTC10(self):
        """
        Verify presence of 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc10() == True

    def testTC11(self):
        """
        Verify presence of 'Earth Science' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc11() == True

    def testTC12(self):
        """
        Verify presence of 'Life Science' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc12() == True

    def testTC13(self):
        """
        Verify presence of 'Physical Science' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc13() == True

    def testTC14(self):
        """
        Verify presence of 'Biology' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc14() == True

    def testTC15(self):
        """
        Verify presence of 'Chemistry' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc15() == True

    def testTC16(self):
        """
        Verify presence of 'Physics' link in the 'Science' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc16() == True

    def testTC17(self):
        """
        Verify presence of 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc17() == True

    def testTC18(self):
        """
        Verify presence of 'Math Grade 6' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc18() == True

    def testTC19(self):
        """
        Verify presence of 'Math Grade 7' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc19() == True

    def testTC20(self):
        """
        Verify presence of 'Math Grade 8' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc20() == True

    def testTC21(self):
        """
        Verify presence of 'Algebra' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc21() == True

    def testTC22(self):
        """
        Verify presence of 'Geometry' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc22() == True

    def testTC23(self):
        """
        Verify presence of 'Algebra II' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc23() == True

    def testTC24(self):
        """
        Verify presence of 'Precalculus' link in the 'Math' tab and it's work
        """
        self.getStaticPage()
        assert self.tap.tc24() == True

    def testTC25(self):
        """
        Verify presence of 'Browse All FlexBooks®' link in the 'CHOOSE YOUR SUBJECT' popup and it's work
        """
        self.getStaticPage()
        assert self.tap.tc25() == True

    def testTC26(self):
        """
        Verify presence of the Hero Image wrap
        """
        self.getStaticPage()
        assert self.tap.el_is_visible(
            TeacherAssistantLocators.HERO_IMAGE) == True

    def testTC27(self):
        """
        Verify presence of 'Every Teacher Deserves an Assistant.' text
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_EVERY_TEACHER_DESERVES,
            'Every Teacher Deserves an Assistant.') == True

    def testTC28(self):
        """
        Verify presence of 'Like any great assistant, here’s what CK-12’s Teacher Assistant helps you do:' text
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_LIKE_ANY_GREAT_ASSISTANT,
            'Like any great assistant, here’s what CK-12’s Teacher Assistant helps you do:') == True

    def testTC29(self):
        """
        Verify presence of '
        Teachers are expected to wear many hats.
        More often than not, there’s not enough time in the day to wear them all.
        We’re here to help teachers get back their time and focus on what they do best: teaching!
        ' text
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_TEACHERS_ARE_EXPECTED,
            'Teachers are expected to wear many hats. More often than not, there’s not enough time in the day to wear them all. We’re here to help teachers get back their time and focus on what they do best: teaching!') == True

    def testTC30(self):
        """
        Verify presence of 'Improve Student Learning Outcomes' text
        """
        self.getStaticPage()
        assert self.tap.verifyElementTextIs(
            TeacherAssistantLocators.TEXT_ISLO,
            'Improve Student Learning Outcomes') == True

    def testTC31(self):
        """
        Verify 'Perfomance Patterns' tab and it's title
        """
        self.getStaticPage()
        assert self.tap.tc31() == True

    def testTC32(self):
        """
        Verify presence of 'Perfomance Patterns' tab icon
        """
        self.getStaticPage()
        assert self.tap.tc32() == True

    def testTC33(self):
        """
        Verify presence of 'Perfomance Patterns' tab title
        """
        self.getStaticPage()
        assert self.tap.tc33() == True

    def testTC34(self):
        """
        Verify presence of 'Perfomance Patterns' tab text
        """
        self.getStaticPage()
        assert self.tap.tc34() == True

    def testTC35(self):
        """
        Verify presence of 'Perfomance Patterns' tab image
        """
        self.getStaticPage()
        assert self.tap.tc35() == True

    def testTC36(self):
        """
        Verify 'Class Insights' tab and it's title
        """
        self.getStaticPage()
        assert self.tap.tc36() == True

    def testTC37(self):
        """
        Verify 'Class Insights' button icon
        """
        self.getStaticPage()
        assert self.tap.tc37() == True

    def testTC38(self):
        """
        Verify 'Class Insights' content icon
        """
        self.getStaticPage()
        assert self.tap.tc38() == True

    def testTC39(self):
        """
        Verify 'Class Insights' title
        """
        self.getStaticPage()
        assert self.tap.tc39() == True

    def testTC40(self):
        """
        Verify 'Class Insights' description
        """
        self.getStaticPage()
        assert self.tap.tc40() == True

    def testTC41(self):
        """
        Verify 'Class Insights' image
        """
        self.getStaticPage()
        assert self.tap.tc41() == True

    def testTC42(self):
        """
        Verify 'Recommendations' tab and it's title
        """
        self.getStaticPage()
        assert self.tap.tc43() == True

    def testTC43(self):
        """
        Verify 'Recommendations' tab button icon
        """
        self.getStaticPage()
        assert self.tap.tc43() == True

    def testTC44(self):
        """
        Verify 'Recommendations' icon
        """
        self.getStaticPage()
        assert self.tap.tc44() == True

    def testTC45(self):
        """
        Verify 'Recommendations' text
        """
        self.getStaticPage()
        assert self.tap.tc45() == True

    def testTC46(self):
        """
        Verify 'Recommendations' description
        """
        self.getStaticPage()
        assert self.tap.tc46() == True

    def testTC47(self):
        """
        Verify 'Recommendations' image
        """
        self.getStaticPage()
        assert self.tap.tc47() == True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    pytest.main()
