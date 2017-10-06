from pywinauto import Desktop

def get_name_from_pycharm():
    pycharm_app = Desktop(backend = 'uia').window(class_name_re = 'SunAwtFrame')
    run_project_name = pycharm_app.texts()[0].split('- [')[0]
    return run_project_name


if __name__ == '__main__':
    print(get_name_from_pycharm())