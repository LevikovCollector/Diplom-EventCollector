from pywinauto import Desktop


def get_url_from_active_tab():
    # Ищем окно у которого в классе встречается Chrome
    chrome_app = Desktop(backend="uia").window(class_name_re = 'Chrome')
    # Получаем wrapper_object строки с юрл
    address_bar_wrapper = chrome_app['Google Chrome'].main.Edit.wrapper_object()
    url_from_browser = address_bar_wrapper.legacy_properties()['Value']
    return url_from_browser


if __name__ == '__main__':
    print(get_url_from_active_tab())
