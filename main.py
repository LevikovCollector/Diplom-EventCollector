from web import get_url_from_active_tab
from datetime import datetime
from pycharm_work_project import get_name_from_pycharm
import bd_work

APPS_LIST = ['Chrome', 'PyCharm']

def main(app):
    additional_info = None
    date = datetime.strptime(str(datetime.now().strftime('%d.%m.%y %H:%M')),'%d.%m.%y %H:%M')


    if app == APPS_LIST[0]:
        additional_info = get_url_from_active_tab()
        bd_work.browser_info_save(APPS_LIST[0], date, additional_info)

    elif app == APPS_LIST[1]:
        additional_info = get_name_from_pycharm()
        bd_work.pycharm_info_save(APPS_LIST[1], date, additional_info)

    bd_work.db_commit()



if __name__ == '__main__':
    main('Chrome')
    main('PyCharm')
