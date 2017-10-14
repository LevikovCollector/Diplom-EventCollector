import psutil
from time import sleep


def check_process():
    chrome_status = False
    chrome_pid = 0
    while 1:

        for proc in psutil.process_iter():
            name = proc.name()

            if name == "chrome.exe":
                chrome_status = True
                chrome_pid = proc.pid
                break
            else:
                chrome_status = False

        if(chrome_status):
            print('Хром запущен!')
            print('ID процесса: {0}'.format(chrome_pid))
        else:
            print('Хром не запущен! Жду 5 сек')
            sleep(5)

def get_info_chrome():
    pass



if __name__ == '__main__':
    check_process()