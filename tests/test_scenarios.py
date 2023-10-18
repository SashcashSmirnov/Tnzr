from Tensor_SBIS.conftest import SBIS_MAIN_PAGE_URL
from Tensor_SBIS.conftest import TENSOR_MAIN_PAGE_URL
from Tensor_SBIS.pages.tensor_page import TensorPage
from Tensor_SBIS.pages.sbis_page import SbisPage


class TestScenario_1():

    def test_go_contacts_go_tensor_banner(self, browser):
        page = SbisPage(browser, SBIS_MAIN_PAGE_URL)
        page.open()
        page.go_to_contacts_page_from_header()
        page.click_to_tensor_banner_in_contacts()

    def test_check_block_sila_v_ludiah_and_block_work(self, browser):
        page = TensorPage(browser, TENSOR_MAIN_PAGE_URL)
        page.open()
        page.find_and_check_block_sila_v_ludiah()
        page.click_to_more_info_in_sila_v_ludiah_block()
        page.check_current_url_is_tensor_ru_about()
        page.find_and_check_block_rabotaem()
        page.check_height_and_width_of_imgs_in_block_work()


class TestScenario_2():
    def test_check_region_in_contacts_def_Sverdlovskaya(self, browser):
        page = SbisPage(browser, SBIS_MAIN_PAGE_URL)
        page.open()
        page.go_to_contacts_page_from_header()
        page.check_region_in_contacts_is_Sverdlovskaya()
        page.check_partners_in_contacts_is_Sverdlovskaya()

    def test_change_region_in_contacts_to_kamchatsky(self, browser):
        page = SbisPage(browser, SBIS_MAIN_PAGE_URL)
        page.open()
        page.go_to_contacts_page_from_header()
        page.go_to_region_change_from_contacts()
        page.change_region_to_Kamchatsky()
        page.check_partners_in_contacts_is_Kamchatsky()
        page.check_current_url_is_Kamchatsky()
        page.check_title_is_Kamchatsky()


class TestScenario_3():
    def test_go_to_sbis_downloads_and_downloadfile(self, browser):
        page = SbisPage(browser, SBIS_MAIN_PAGE_URL)
        page.open()
        page.go_to_download_sbis_page_from_main_page()
        page.check_file_size()
