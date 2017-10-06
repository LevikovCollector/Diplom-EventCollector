from db_conf import db_session, Info_Data



def browser_info_save(app_name, date, url):
    browser_info = Info_Data(app_name = app_name, timestamp = date, active_tab_url = url)
    db_session.add(browser_info)

def pycharm_info_save(app_name, date, project_name):
    pycharm_info = Info_Data(app_name = app_name, timestamp = date, pycharm_project = project_name)
    db_session.add(pycharm_info)

def db_commit():
    db_session.commit()

if __name__ == '__main__':
    #
    url = get_url_from_active_tab()
    project = get_name_from_pycharm()
    app = ['Chrome', 'PyCharm']
    date = datetime.now().strftime('%d.%m.%y %H:%M')

    pass