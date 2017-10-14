from get_info_from_app import get_url_from_active_tab, get_name_from_pycharm, get_path_file_sublime_text
from datetime import datetime
import db_work

APPS_LIST = ['Chrome', 'PyCharm', 'Sublime']


def main(app):
    additional_info = None
    date = datetime.strptime(str(datetime.now().strftime('%d.%m.%y %H:%M')),'%d.%m.%y %H:%M')
    data_add_status = False

    if app == APPS_LIST[0]:
        additional_info = get_url_from_active_tab()
        db_work.browser_info_save(APPS_LIST[0], date, additional_info)
        data_add_status = True

    elif app == APPS_LIST[1]:
        additional_info = get_name_from_pycharm()
        db_work.pycharm_info_save(APPS_LIST[1], date, additional_info)
        data_add_status = True

    elif app == APPS_LIST[2]:
        additional_info = get_path_file_sublime_text()
        db_work.sublime_info_save(APPS_LIST[2], date, additional_info)
        data_add_status = True

    if(data_add_status):
        db_work.db_commit()


if __name__ == '__main__':
    pass