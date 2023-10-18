import time
import os
import logging
from Tensor_SBIS.pages.base_page import BasePage
from Tensor_SBIS.locators.locators import SbisPageLocators
from Tensor_SBIS.pages.file_size_checker import bt_to_mb_conv


for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log.txt',
                    filemode='a')


class SbisPage(BasePage):
    locators = SbisPageLocators()

    def go_to_contacts_page_from_header(self):
        logging.info("Клик на 'Контакты' в хедере")
        self.element_is_visible(self.locators.CONTACTS_LINK_HEADER).click()
        logging.info("Открыты 'Контакты'")

    def click_to_tensor_banner_in_contacts(self):
        logging.info("Клик на баннер 'Тензор' в контактах")
        self.element_is_clickable(
            self.locators.BANNER_TENSOR_IN_CONTACTS).click()
        logging.info("Произошел переход на сайт Тензор")

    def check_region_in_contacts_is_Sverdlovskaya(self):
        logging.info("Проверка что установлен регион - Свердловская обл.")
        region = self.element_is_visible(self.locators.REGION_IN_CONTACTS).text
        assert region == 'Свердловская обл.', "Регион отличается от заданного(Свердловская обл.)"
        logging.info("Верно! Регион - Свердловская обл.")

    def check_partners_in_contacts_is_Sverdlovskaya(self):
        logging.info("Проверка что партнеры из Свердловской обл.")
        partners = self.element_is_visible(self.locators.PARTNERS_LIST).text
        assert partners == 'Екатеринбург', "Партнеры отличаются от заданного(Свердловская обл.)"
        logging.info("Верно! Партнеры из Свердловской обл.")

    def go_to_region_change_from_contacts(self):
        logging.info("Клик на текущий установленный регион для его изменения")
        self.element_is_clickable(self.locators.REGION_IN_CONTACTS).click()

        logging.info("Открыто окно для смены региона")

    def change_region_to_Kamchatsky(self):
        logging.info("Клик в окне выбора региона на Камчатский край")
        self.element_is_visible(self.locators.REGION_SELECT_KAMCHATSKY).click()
        logging.info("Выбран Камчатский край")

    def check_region_in_contacts_is_Kamchatsky(self):
        logging.info("Проверка что установлен регион - Камчатский край")
        region = self.element_is_visible(self.locators.REGION_IN_CONTACTS).text
        assert region == 'Камчатский край', "Регион отличается от заданного(Камчатский край)"
        logging.info("Верно! Установленый регион - Камчатский край")

    def check_partners_in_contacts_is_Kamchatsky(self):
        logging.info("Проверка что партнеры из Камчатского края")
        time.sleep(1)
        partners = self.element_is_visible(self.locators.PARTNERS_LIST).text
        assert partners == 'Петропавловск-Камчатский', "Партнеры отличаются от заданного(Петропавловск-Камчатский)"
        logging.info("Верно! Партнеры из Камчатского края")

    def check_current_url_is_Kamchatsky(self):
        logging.info("Проверка что в урл указан Камчатский край")
        url = self.driver.current_url
        assert url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients", "Текущая ссылка не 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients'!"
        logging.info("Верно! в урл Камчатский край")

    def check_title_is_Kamchatsky(self):
        logging.info("Проверка что в тайтл указан Камчатский край")
        title = self.driver.title
        assert title == 'СБИС Контакты — Камчатский край', "Тайтл не соответствует требуемому (СБИС Контакты — Камчатский край)!"
        logging.info("Верно! в в тайтл указан Камчатский край")

    def go_to_download_sbis_page_from_main_page(self):
        logging.info("Клик на 'Скачать сбис' в футере")
        self.element_is_visible(
            self.locators.DOWNLOAD_LINK_FOOTER).click()
        logging.info("Открыта страница Сбис - 'Скачать' ")
        logging.info("Клик в меню на 'СБИС Плагин'")
        time.sleep(1)
        link = self.element_is_visible(
            self.locators.SBIS_PLUGIN_LINK)
        self.driver.execute_script("arguments[0].click();", link)
        logging.info("Перешли в меню 'СБИС плагин'")
        logging.info("Скачиваем 'Веб-установщик'")
        link = self.element_is_present(
            self.locators.DOWNLOAD_FILE_BUTTON).click()
        logging.info("Файл 'Веб-установщик' сохранен")

    def check_file_size(self):
        time.sleep(3)
        logging.info("Проверка размера скачанного файла.")
        file_size_bt = os.path.getsize(
            "C:\\Users\\Alex\\Python\\Tensor_SBIS\\download\\sbisplugin-setup-web.exe")
        size = bt_to_mb_conv(file_size_bt)
        assert size == '3.64', "Размер файла не соответствует указанному на сайте — 3.64 МБ"
        logging.info("Скачанный файл прошел проверку на соответствие размера.")
