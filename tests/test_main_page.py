from selenium import webdriver
from pages import main_page
from pages.main_page import MainPage


class TestMainPage:
    mp = None
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('https://qa-scooter.praktikum-services.ru/')
        cls.mp = MainPage(cls.driver)
        cls.mp.click_cookie_button()

    def test_first_question(self):
        self.mp.click_question(self.mp.first_question)
        self.mp.check_text_answer(self.mp.first_answer, self.mp.first_answer_text)

    def test_second_question(self):
        self.mp.click_question(self.mp.second_question)
        self.mp.check_text_answer(self.mp.second_answer, self.mp.second_answer_text)
    '''
    def test_third_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.third_question)
        mp.check_text_answer(mp.third_answer, mp.third_answer_text)

    def test_fourth_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.fourth_question)
        mp.check_text_answer(mp.fourth_answer, mp.fourth_answer_text)

    def test_fifth_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.fifth_question)
        mp.check_text_answer(mp.fifth_answer, mp.fifth_answer_text)

    def test_sixth_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.sixth_question)
        mp.check_text_answer(mp.sixth_answer, mp.sixth_answer_text)

    def test_seventh_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.seventh_question)
        mp.check_text_answer(mp.seventh_answer, mp.seventh_answer_text)

    def test_eighth_question(self):
        mp = MainPage(self.driver)
        mp.click_cookie_button()
        mp.click_question(mp.eighth_question)
        mp.check_text_answer(mp.eighth_answer, mp.eighth_answer_text)
    '''

    @classmethod
    def teardown(cls):
        cls.driver.quit()
