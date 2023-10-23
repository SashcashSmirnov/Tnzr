from selenium.webdriver.common.by import By


class SbisPageLocators:
    TARIFS_LINK_HEADER = (
        By.CSS_SELECTOR, 'li[class="sbisru-Header__menu-item sbisru-Header__menu-item-0 mh-8  s-Grid--hide-sm"]')
    CONTACTS_LINK_HEADER = (
        By.CSS_SELECTOR, 'li[class="sbisru-Header__menu-item sbisru-Header__menu-item-1 mh-8  s-Grid--hide-sm"]')
    SUPPORT_LINK_HEADER = (
        By.CSS_SELECTOR, 'li[class="sbisru-Header__menu-item sbisru-Header__menu-item-2 mh-8  s-Grid--hide-sm"]')
    START_WORK_LINK_HEADER = (
        By.CSS_SELECTOR, 'li[class="sbisru-Header__menu-item sbisru-Header__menu-item-3 mh-8 sbisru-Header__menu-item--99"]')
    BANNER_TENSOR_IN_CONTACTS = (
        By.CSS_SELECTOR, 'img[alt="Разработчик системы СБИС — компания «Тензор»"]')
    REGION_IN_CONTACTS = (
        By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    PARTNERS_LIST = (
        By.CSS_SELECTOR, '[class="sbisru-Contacts-List__city sbisru-text--standart sbisru-Contacts__text--500 sbisru-Contacts__text--md-xm pl-24 pl-xm-0 pt-16 pt-xm-12 pb-4 pb-xm-8 ws-flexbox ws-justify-content-between ws-align-items-start"]')
    REGION_SELECT_KAMCHATSKY = (
        By.CSS_SELECTOR, 'span[title="Камчатский край"]')
    HTML = (By.XPATH, '//h2[text()="Контакты"]')
    DOWNLOAD_LINK_FOOTER = (By.XPATH, '//a[text()="Скачать СБИС"]')
    SBIS_PLUGIN_LINK = (By.XPATH, '//div[text()="СБИС Плагин"]')
    DOWNLOAD_FILE_BUTTON = (
        By.XPATH, '//a[text()="Скачать (Exe 3.65 МБ) "]')


class TensorPageLocators:
    SILA_V_LUDIAH_BLOCK = (
        By.XPATH, '//p[text()="Сила в людях"]')
    WORKIN_BLOCK = (By.XPATH, '//h2[text()="Работаем"]')
    SILA_V_LUDIAH_BLOCK_PODROBNEE_LINK = (
        By.XPATH, '//a[@href="/about" and @class="tensor_ru-link tensor_ru-Index__link"]')
    ALL_FOUR_IMGS_WORKIN_BLOCK = (
        By.CSS_SELECTOR, 'img[class="tensor_ru-About__block3-image new_lazy loaded"]')
