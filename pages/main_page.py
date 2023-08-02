from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:

    cookie_button = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    yandex_logo = [By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]/img']
    question_header = [By.XPATH, '//div[text()="Вопросы о важном"]']

    first_question = [By.ID, 'accordion__heading-0']
    first_answer = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    first_answer_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    second_question = [By.ID, 'accordion__heading-1']
    second_answer = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    second_answer_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    third_question = [By.ID, 'accordion__heading-2']
    third_answer = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    third_answer_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    fourth_question = [By.ID, 'accordion__heading-3']
    fourth_answer = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    fourth_answer_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    fifth_question = [By.ID, 'accordion__heading-4']
    fifth_answer = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    fifth_answer_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    sixth_question = [By.ID, 'accordion__heading-5']
    sixth_answer = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    sixth_answer_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    seventh_question = [By.ID, 'accordion__heading-6']
    seventh_answer = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    seventh_answer_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    eighth_question = [By.ID, 'accordion__heading-7']
    eighth_answer = [By.XPATH, '//div[@id="accordion__panel-7"]/p']
    eighth_answer_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    def __init__(self, driver):
        self.driver = driver

    def click_question(self, question):
        return self.driver.find_element(*question).click()

    def check_text_answer(self, answer, text):
        actually_value = self.driver.find_element(*answer).text
        expected_value = text
        assert actually_value == expected_value

    '''
    def wait_cookie_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(*self.cookie_button))
    '''

    def click_cookie_button(self):
        self.driver.find_element(*self.cookie_button).click()

    def check_yandex_logo(self):
        actually_value = self.driver.find_element(*self.yandex_logo).get_property('alt')
        expected_value = 'Yandex'
        assert actually_value == expected_value
