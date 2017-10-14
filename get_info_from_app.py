from pywinauto import Desktop


def get_url_from_active_tab():
    # Ищем окно у которого в классе встречается Chrome
    chrome_app = Desktop(backend = "uia").window(class_name_re = 'Chrome')
    # Получаем wrapper_object строки с юрл
    address_bar_wrapper = chrome_app['Google Chrome'].main.Edit.wrapper_object()
    url_from_browser = address_bar_wrapper.legacy_properties()['Value']
    return url_from_browser


def get_name_from_pycharm():
    pycharm_app = Desktop(backend = 'uia').window(class_name_re = 'SunAwtFrame')
    run_project_name = pycharm_app.texts()[0].split('- [')[0]
    return run_project_name


def get_path_file_sublime_text():
    sublime_app = Desktop(backend = 'uia').window(class_name_re = 'PX_WINDOW_CLASS')
    title_app = sublime_app.texts()[0].split(' - ')[0].split(' ')
    path_to_sublime_file = title_app[0]
    return path_to_sublime_file


if __name__ == '__main__':
    print(get_path_file_sublime_text())
    print(get_name_from_pycharm())
    print(get_url_from_active_tab())
