from db_conf import db_session, Info_Data


def browser_info_save(app_name, date, url):
    browser_info = Info_Data(app_name = app_name, timestamp = date, active_tab_url = url)
    db_session.add(browser_info)


def pycharm_info_save(app_name, date, project_name):
    pycharm_info = Info_Data(app_name = app_name, timestamp = date, pycharm_project = project_name)
    db_session.add(pycharm_info)


def sublime_info_save(app_name, date, path):
    sublime_info = Info_Data(app_name = app_name, timestamp = date, sublime_path = path)
    db_session.add(sublime_info)


def db_commit():
    db_session.commit()


def not_send_info():
    info = Info_Data()
    return info.query.filter(Info_Data.send_status == False).all()


if __name__ == '__main__':
    pass