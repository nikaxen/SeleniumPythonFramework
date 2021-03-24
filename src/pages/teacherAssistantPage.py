from selenium import webdriver
from pages.basePage import BasePage
from locators.teacherAssistantLocators import TeacherAssistantLocators
import time


class teacherAssistantPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def getBackToTheFirstTab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def tc6(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP) == True:
            return True
        else:
            return False

    def tc7(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_CLOSE).click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP) == True:
            return True
        else:
            return False

    def tc8(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_TITLE) == True:
            return True
        else:
            return False

    def tc9(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_DESC) == True:
            return True
        else:
            return False

    def tc10(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_EARTH_SCIENCE) == True:
            return True
        else:
            return False

    def tc11(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_EARTH_SCIENCE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Earth Science for Middle School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc12(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_LIFE_SCIENCE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Life Science for Middle School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc13(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_PHYSICAL_SCIENCE).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Physical Science for Middle School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc14(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_BIOLOGY).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Biology for High School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc15(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_CHEMISTRY).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Chemistry for High School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc16(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_SCIENCE_TAB_PHYSICS).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Physics for High School | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc17(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        if self.el_is_visible(
                TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_MG6) == True:
            return True
        else:
            return False

    def tc18(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_MG6).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Middle School Math 6 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc19(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_MG7).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Middle School Math 7 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc20(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_MG8).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Middle School Math 8 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc21(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_ALGEBRA).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Algebra 1 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc22(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_GEOMETRY).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Geometry | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc23(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_ALGEBRA_II).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Interactive Algebra 2 - 2019 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc24(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB).click()
        self.el_is_presented(
            TeacherAssistantLocators.CHOOSE_YOUR_SUBJECT_POPUP_MATH_TAB_PRECALCULUS).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'CK-12 Precalculus Concepts 2.0 | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc25(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.LINK_CHOOSE_YOUR_SUBJECT)
        element.click()
        self.el_is_presented(
            TeacherAssistantLocators.BROWSE_ALL_FLEXBOOKS_IN_CYS_POPUP).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        if self.driver.title == 'FlexBooks® | CK-12 Foundation':
            self.getBackToTheFirstTab()
            return True
        else:
            self.getBackToTheFirstTab()
            return False

    def tc31(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_PERFOMANCE_PATTERNS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.CLP_TEXT)
        if element_2.text == 'Class-Level Patterns':
            return True
        else:
            return False

    def tc32(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_PERFOMANCE_PATTERNS)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.CLP_ICON):
            return True
        else:
            return False

    def tc33(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_PERFOMANCE_PATTERNS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.CLP_TITLE)
        if element_2.text == 'See Patterns in Your Students’ Skill Levels':
            return True
        else:
            return False

    def tc34(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_PERFOMANCE_PATTERNS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.CLP_DESC)
        if element_2.text == 'The Teacher Assistant shows you how your students’ engagement is affecting their skill levels and which students need help before moving on to the next lesson.':
            return True
        else:
            return False

    def tc35(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_PERFOMANCE_PATTERNS)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.CLP_IMAGE):
            return True
        else:
            return False

    def tc36(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.TCI_TEXT)
        if element_2.text == 'Class Insights':
            return True
        else:
            return False

    def tc37(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        if self.el_is_visible(
                TeacherAssistantLocators.TAB_CLASS_INSIGHTS_ICON):
            return True
        else:
            return False

    def tc38(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.TCI_ICON):
            return True
        else:
            return False

    def tc39(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.TCI_TITLE)
        if element_2.text == 'Pinpoint Where Your Students Are Struggling':
            return True
        else:
            return False

    def tc40(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        element_2 = self.el_is_presented(TeacherAssistantLocators.TCI_DESC)
        if element_2.text == 'The Teacher Assistant uncovers your students’ learning gaps and misconceptions, giving you personalized insights on where you can intervene effectively.':
            return True
        else:
            return False

    def tc41(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.TAB_CLASS_INSIGHTS)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.TCI_IMAGE):
            return True
        else:
            return False

    def tc42(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        element_2 = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TEXT)
        if element_2.text == 'Recommendations':
            return True
        else:
            return False

    def tc43(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        if self.el_is_visible(
                TeacherAssistantLocators.RECOMMENDATIONS_TAB_ICON):
            return True
        else:
            return False

    def tc44(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.RECOMMENDATIONS_ICON):
            return True
        else:
            return False

    def tc45(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        element_2 = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TITLE)
        if element_2.text == 'Get Actionable Recommendations':
            return True
        else:
            return False

    def tc46(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        element_2 = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_DESC)
        if element_2.text == 'The Teacher Assistant provides actionable recommendations to help improve your students’ learning outcomes, including specific problem areas to close any learning gaps.':
            return True
        else:
            return False

    def tc47(self):
        element = self.el_is_presented(
            TeacherAssistantLocators.RECOMMENDATIONS_TAB)
        element.click()
        if self.el_is_visible(TeacherAssistantLocators.RECOMMENDATIONS_IMAGE):
            return True
        else:
            return False
