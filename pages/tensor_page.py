import logging
from Tensor_SBIS.pages.base_page import BasePage
from Tensor_SBIS.locators.locators import TensorPageLocators


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.txt',
                    filemode='a')


class TensorPage(BasePage):
    locators = TensorPageLocators()

    def find_and_check_block_sila_v_ludiah(self):
        logging.info("Проверка на наличие блока 'Сила в людях'")
        block_sila_v_ludiah_ = self.element_is_visible(
            self.locators.SILA_V_LUDIAH_BLOCK).text
        assert block_sila_v_ludiah_ == 'Сила в людях', "Блок с названием 'Сила в людях' не найден."
        logging.info("Блок 'Сила в людях' найден.")

    def click_to_more_info_in_sila_v_ludiah_block(self):
        logging.info("Клик на кнопку 'Подробнее' в блоке 'Сила в людях'")
        self.element_is_present(
            self.locators.SILA_V_LUDIAH_BLOCK_PODROBNEE_LINK).click()
        logging.info("Перешли на страницу 'Подробнее'")

    def check_current_url_is_tensor_ru_about(self):
        logging.info("Проверка что урл - https://tensor.ru/about")
        url = self.driver.current_url
        assert url == "https://tensor.ru/about", "Текущая ссылка не 'https://tensor.ru/about'!"
        logging.info("Верно! урл - https://tensor.ru/about")

    def find_and_check_block_rabotaem(self):
        logging.info("Проверка на наличие блока 'Работаем'")
        block_rabotaem = self.element_is_visible(
            self.locators.WORKIN_BLOCK).text
        assert block_rabotaem == 'Работаем', "Блок с названием 'Работаем' не найден."
        logging.info("Блок 'Работа' найден.")

    def check_height_and_width_of_imgs_in_block_work(self):
        logging.info(
            "Поиск и проверка размера четырех изображений в блоке 'Работаем'")
        pics = self.elements_are_visible(
            self.locators.ALL_FOUR_IMGS_WORKIN_BLOCK)
        for pic in pics:
            assert pic.size == {
                'height': 194, 'width': 272}, "Высота и ширина изображений не соответствуют заданным"
        logging.info("Все четыре изображения одного размера!")
